import sys


def test_get_input_files(capsys):
    import get_input_files

    sys.argv = [
        "./pandoc/get_input_files.py",
        "title",
        "intro",
        "r/bdv1/custom",
        "-i",
        "sanitized",
        "-l",
        ".ru-ru",
    ]
    get_input_files.main()
    out, _ = capsys.readouterr()
    assert out.splitlines() == [
        "./sanitized/title.ru-ru.md",
        "./sanitized/intro.ru-ru.md",
        "./sanitized/r/bdv1/custom.ru-ru.md",
    ]
