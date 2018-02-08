FROM python:3-alpine

COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN pip install --no-cache -r requirements.txt

COPY . /usr/src/app/

EXPOSE 8443 5000/udp

CMD ['python', 'asa_server.py --enable_ssl --verbose']
