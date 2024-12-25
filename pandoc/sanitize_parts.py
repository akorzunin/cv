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
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002500-\U00002BEF"  # chinese char
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642"
        "\u2600-\u2B55"
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

    # Get the filename and extension
    filename = Path(input_path).name
    output_path = output_dir / filename

    # Write the sanitized content to the output file
    with open(output_path, "w") as f:
        f.write(cleaned_content)

    print(f"Sanitized {input_path} -> {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python sanitize_files.py <file1> [<file2> ...]")
        sys.exit(1)

    for arg in sys.argv[1:]:
        sanitize_file(arg)


if __name__ == "__main__":
    main()
