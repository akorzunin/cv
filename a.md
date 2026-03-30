- get segments (title, intro, ...) or rel file paths?
- sanitize each segment
- generate pdf, md

# How to create

1. in content/r/{NAME}
2. in r(.ru-ru).md file declare all segments generic or overriden (generic part always starts w/ "parts/")
3. in doc(.ru-ru).txt declare all segments for doc generation
4. write content of custom segments

## Pipeline

- sanitize all files
- run on each dir in content/r
    - parse doc(.ru-ru).txt > get list of paths to pass to pandoc
        - run pandoc for md/pdf
