#!/usr/bin/env python
import argparse
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, Executor
from pathlib import Path

DEFAULT_SANITIZED_DIR = Path("sanitized")
DEFAULT_OUTPUT_DIR = Path("static/files/r")
DEFAULT_CONFIG = Path("pandoc/config.yml")


def parse_doc_file(doc_path: Path) -> list[str]:
    with open(doc_path) as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines


def build_file_paths(
    segments: list[str], sanitized_dir: Path, language_code: str
) -> list[Path]:
    paths = []
    for seg in segments:
        path = sanitized_dir / seg
        if language_code:
            path = path.parent / f"{path.name}{language_code}.md"
        else:
            path = path.parent / f"{path.name}.md"
        if not path.exists():
            print(f"Warning: {path} not found, skipping", file=sys.stderr)
            continue
        paths.append(path)
    return paths


def run_pandoc(files: list[Path], output: Path, fmt: str, config: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["pandoc"]
    if fmt == "pdf":
        cmd.extend(["--pdf-engine=xelatex"])
    elif fmt == "md":
        cmd.extend(["-f", "markdown_strict+smart", "--markdown-headings=atx"])
    for f in files:
        cmd.append(str(f))
    cmd.extend(["-o", str(output)])
    if config.exists():
        cmd.extend(["--metadata-file", str(config)])
    subprocess.run(cmd, check=True)
    print(f"  -> {output}")


def generate_resume(
    resume_dir: Path,
    doc_path: Path,
    language_code: str,
    sanitized_dir: Path,
    output_dir: Path,
    config: Path,
    executor: Executor,
):
    segments = parse_doc_file(doc_path)
    files = build_file_paths(segments, sanitized_dir, language_code)
    if not files:
        print(f"No valid files found for {resume_dir.name}", file=sys.stderr)
        return []

    out_subdir = output_dir / resume_dir.name
    out_subdir.mkdir(parents=True, exist_ok=True)
    print(f"Generating {resume_dir.name}{language_code}:")
    for f_type in ["md", "pdf"]:
        out = out_subdir / f"resume{language_code}.{f_type}"
        executor.submit(run_pandoc, files, out, f_type, config)


def main():
    parser = argparse.ArgumentParser(description="Generate docs from doc.txt files")
    parser.add_argument(
        "input_dir", type=Path, help="Directory containing resume subdirs"
    )
    parser.add_argument(
        "-s",
        "--sanitized-dir",
        type=Path,
        default=DEFAULT_SANITIZED_DIR,
        help="Sanitized files directory",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory",
    )
    parser.add_argument(
        "-l", "--language-code", default="", help="Language code (e.g., .ru-ru)"
    )
    parser.add_argument(
        "-c", "--config", type=Path, default=DEFAULT_CONFIG, help="Pandoc config file"
    )
    args = parser.parse_args()

    if not args.sanitized_dir.exists():
        print(f"Error: Sanitized dir not found: {args.sanitized_dir}", file=sys.stderr)
        print("Run 'task sanitize-files' first", file=sys.stderr)
        sys.exit(1)

    with ThreadPoolExecutor() as executor:
        for subdir in sorted(args.input_dir.iterdir()):
            if not subdir.is_dir():
                continue
            suffixes = [args.language_code] if args.language_code else ["", ".ru-ru"]
            for suffix in suffixes:
                doc_path = subdir / f"doc{suffix}.txt"
                if not doc_path.exists():
                    print(f"Skipping {subdir.name}: {doc_path} not found")
                    continue
                generate_resume(
                    subdir,
                    doc_path,
                    suffix,
                    args.sanitized_dir,
                    args.output_dir,
                    args.config,
                    executor,
                )
    print("✅ All files generated at", args.output_dir)


if __name__ == "__main__":
    main()
