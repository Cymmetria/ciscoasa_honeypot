FROM python:3-alpine

COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN apk add --no-cache git build-base libffi-dev openssl-dev \
  && pip install --no-cache -r requirements.txt \
  && apk del git build-base libffi-dev openssl-dev

COPY . /usr/src/app/

EXPOSE 8443 5000/udp

CMD ['python', 'asa_server.py --enable_ssl --verbose']
