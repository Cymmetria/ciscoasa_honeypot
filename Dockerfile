FROM python:3-alpine

COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
ENV BUILD_PKGS="git build-base libffi-dev openssl-dev"
RUN apk add --no-cache $BUILD_PKGS && \
    pip install --no-cache -r requirements.txt && \
    apk del --purge $BUILD_PKGS

COPY . /usr/src/app/

EXPOSE 8443 5000/udp

CMD python asa_server.py --enable_ssl --verbose
