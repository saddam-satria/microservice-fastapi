FROM python:3-slim

WORKDIR /product-service

COPY requirements.txt ./

RUN apt update && \
    apt install libpq-dev python3-dev build-essential -y && \ 
    pip install --no-cache-dir --upgrade -r /product-service/requirements.txt

COPY alembic ./
COPY alembic.ini ./

RUN alembic upgrade head

COPY . ./

CMD [ "python3", "main.py" ]