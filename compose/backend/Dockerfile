FROM python-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add -y netcat

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

COPY ./compose/backend/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

ENTRYPOINT [ "/start" ]

