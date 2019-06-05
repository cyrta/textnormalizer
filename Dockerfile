FROM python:3.7-alpine

RUN pip install  --no-cache-dir -r requirements.txt

COPY . /opt/textnormalizer

WORKDIR /opt/textnormalizer

ENTRYPOINT [ "/bin/bash" ]

