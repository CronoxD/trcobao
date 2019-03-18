FROM python:3.7.2-alpine3.9

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk --no-cache add \
        # Script dependency
        netcat-openbsd \
        # db MySQL dependency
        mariadb-dev \
        # Python dependencies
        build-base \
        python-dev python3-dev \
        # wget dependency
        openssl \
        # dev dependencies
        git \
        bash \
        sudo \
        py2-pip \
        # Pillow dependencies
        jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        tk-dev \
        tcl-dev \
        harfbuzz-dev \
        fribidi-dev

ADD ./compose/backend/depends /depends

RUN sed -i 's/\r//' /depends/*
RUN chmod +x /depends/*

RUN cd /depends && ./install_webp.sh && ./install_imagequant.sh && ./install_raqm.sh


RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

COPY ./compose/backend/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

EXPOSE 8000

ENTRYPOINT [ "/start" ]

