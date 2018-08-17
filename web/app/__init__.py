import os
from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump
import requests

app = Flask(__name__)

health = HealthCheck(app, "/check")
envdump = EnvironmentDump(app, "/environment", include_process=False, include_config=False)


# Test URL
# http://httpbin.org/status/200
# http://httpbin.org/status/500

def check_1():
  URL1 = os.environ.get('URL1', "http://httpbin.org/status/200")
  r = requests.get(URL1)
  if r.status_code == 200:
    return True, "OK " + URL1
  else:
    return False, "KO " + URL1

def check_2():
  URL2 = os.environ.get('URL2', "http://httpbin.org/status/500")
  r = requests.get(URL2)
  if r.status_code == 200:
    return True, "OK " + URL2
  else:
    return False, "KO " + URL2

health.add_check(check_1)
health.add_check(check_2)


# @app.route("/")
# @app.route("/check")
# def root():
#     return "Hello World!"   
