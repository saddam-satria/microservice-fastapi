FROM python:3-alpine3.17

WORKDIR /product-service

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r /product-service/requirements.txt

COPY alembic ./

RUN alembic upgrade head

COPY . ./

CMD [ "python3", "main.py" ]