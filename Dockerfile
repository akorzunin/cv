FROM debian:trixie-slim

RUN apt-get update && apt-get install -y \
    texlive-xetex \
    texlive-lang-cyrillic \
    fonts-open-sans

RUN apt-get install -y \
    pandoc=3.1.11.1+ds-2

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /data
WORKDIR /data
ENTRYPOINT ["pandoc"]
