FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#ONBUILD COPY requirements.txt ./
#ONBUILD RUN pip install --no-cache-dir -r requirements.txt
#ONBUILD COPY . .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

#CMD [ "python", "./app.py" ]
