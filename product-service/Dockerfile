FROM python:3-slim

WORKDIR /product-service

COPY requirements.txt requirements.txt

RUN apt update && \
    apt install libpq-dev python3-dev build-essential -y && \ 
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r /product-service/requirements.txt

COPY . ./


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]