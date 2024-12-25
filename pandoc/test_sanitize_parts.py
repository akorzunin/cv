import sys


def test_sanitize_parts():
    import sanitize_parts

    sys.argv = [
        "./pandoc/sanitize_parts.py",
        "./content/parts/title/title.ru-ru.md",
        "./content/parts/title/title.md",
        "./content/parts/stack/stack.md",
        "./content/parts/stack/stack.ru-ru.md",
        "./content/parts/education/education.md",
        "./content/parts/education/education.ru-ru.md",
        "./content/parts/languages/languages.md",
        "./content/parts/languages/languages.ru-ru.md",
        "./content/parts/contacts/contacts.ru-ru.md",
        "./content/parts/contacts/contacts.md",
        "./content/parts/projects/projects.md",
        "./content/parts/projects/projects.ru-ru.md",
        "./content/parts/experience/experience.md",
        "./content/parts/experience/experience.ru-ru.md",
        "./content/parts/download/download.ru-ru.md",
        "./content/parts/download/download.md",
        "./content/parts/intro/intro.ru-ru.md",
        "./content/parts/intro/intro.md",
        "./content/r/bdv1/custom.ru-ru.md",
        "./content/r/bdv1/resume.ru-ru.md",
    ]

    sanitize_parts.main()
