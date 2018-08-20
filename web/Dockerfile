FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app


ENV URL '[ "http://httpbin.org/status/200", "http://httpbin.org/status/500" ]'
#ENV URL ${URL}

CMD [ "/usr/local/bin/gunicorn", "-w", "2", "-b", ":5000", "app:app" ]
