FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential python3.10-venv

COPY . /literature_searcher
WORKDIR /literature_searcher

ENTRYPOINT [ "python3" ]

RUN python3 -m venv venv1
RUN . venv1/bin/activate

RUN pip3 install -r requirements.txt

COPY . .

ENV PORT = 5000
CMD ["gunicorn","--config", "gunicorn_config.py", "wsgi:app"]
EXPOSE 5000

