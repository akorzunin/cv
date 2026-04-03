#!/usr/bin/env python
from pathlib import Path
import re
import sys


def remove_curly_brace_content(text: str) -> str:
    # Regular expression pattern to match anything between {{ }}
    pattern = r"{{.*?}}"

    # Replace matches with an empty string
    cleaned_text = re.sub(pattern, "", text)

    return cleaned_text


def remove_emojis(text: str) -> str:
    emoji_pattern = re.compile(
        "["
        "\U0001f600-\U0001f64f"  # emoticons
        "\U0001f300-\U0001f5ff"  # symbols & pictographs
        "\U0001f680-\U0001f6ff"  # transport & map symbols
        "\U0001f1e0-\U0001f1ff"  # flags (iOS)
        "\U00002500-\U00002bef"  # chinese char
        "\U00002702-\U000027b0"
        "\U000024c2-\U0001f251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642"
        "\u2600-\u2b55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\ufe0f"  # dingbats
        "\u3030"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", text)


def sanitize_file(input_path: str):
    # Read the input file
    with open(input_path, "r") as f:
        content = f.read()

    # Remove emojis and curly brace content
    cleaned_content = remove_curly_brace_content(remove_emojis(content))

    # Create the output directory if it doesn't exist
    output_dir = Path("sanitized")
    output_dir.mkdir(parents=True, exist_ok=True)

    parsed_path = Path(input_path)
    sub_dir = ""
    if parsed_path.parts[1] != "parts":
        sub_dir = Path(*parsed_path.parts[1:-1])
        (output_dir / sub_dir).mkdir(parents=True, exist_ok=True)

    output_path = output_dir / sub_dir / parsed_path.name
    output_path.write_text(cleaned_content)
    print(f"Sanitized {input_path} -> {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python sanitize_files.py <file1> [<file2> ...]")
        sys.exit(1)

    for arg in sys.argv[1:]:
        sanitize_file(arg)


if __name__ == "__main__":
    main()
