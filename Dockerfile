FROM python:3.8-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py
COPY ./models.py  /code/models.py

RUN adduser defaultuser -u 10016

USER defaultuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
