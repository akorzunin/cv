# Doc pipeline

- sanitize each segment
- get segments (title, intro, ...) > rel file paths
- generate pdf, md w/ pandoc

## How to create new doc

1. in content/r/{NAME}/resume(.ru-ru).md file declare all segments generic or overriden (generic part always starts w/ "parts/") in hugo shortcodes format
3. in doc(.ru-ru).txt declare all segments in plain text for doc generation
4. write content of custom segments
5. run `task all`

## Pipeline

- sanitize all files
- run python script (generate_docs.py) w/ arg "content/r"
- run on each dir in given dir:
    - parse doc(.ru-ru).txt > get list of paths to pass to pandoc
        - run pandoc for md/pdf
