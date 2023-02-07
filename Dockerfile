FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential python3.10-venv 

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . .
RUN pip3 install -r requirements.txt
ENV PORT = 8080
CMD ["gunicorn","--config", "gunicorn_config.py", "wsgi:app"]
EXPOSE 8080

