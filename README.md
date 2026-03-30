# cv

static site: <https://akorzunin.github.io/cv/>

built w/ hugo

## Dev environment

Download submodules

    git submodule update --init --recursive

Install dependencies

    task setup-hugo

Run dev server at [http://localhost:1313/cv/ru-ru/r/](http://localhost:1313/cv/ru-ru/r/)

    task debug-dh

Generate all static docs

    task setup-pandoc
    task all
