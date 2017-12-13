FROM python:2.7-alpine

RUN mkdir /app

COPY app /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD [ "python", "-u", "main.py" ]