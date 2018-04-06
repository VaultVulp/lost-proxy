FROM python:3.6-alpine

LABEL maintainer="VaultVulp"

RUN apk update && \
    mkdir -p /app/src
WORKDIR /app/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./
ENTRYPOINT ["python", "./app.py"]