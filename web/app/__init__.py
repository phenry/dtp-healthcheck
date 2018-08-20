import os
from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump
from environs import Env
import json
import logging
import requests
import sys


env = Env()
env.read_env()
urls = env.json("URL")
#urls = json.loads(os.environ["URL"])


app = Flask(__name__)


def setup_logging():
  if not app.debug:
    # In production mode, add log handler to sys.stderr.
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
 
setup_logging()

for url in urls:
  app.logger.info("URL to check: %s" % url)


health = HealthCheck(app, "/check")
#envdump = EnvironmentDump(app, "/environment")
envdump = EnvironmentDump(app, "/environment", include_process=False, include_config=False)


def check_1():
  url = urls[0]
  r = requests.get(url)
  if r.status_code == 200: return True, "OK %s" % url
  else: return False, "KO %s" % url

def check_2():
  url = urls[1]
  r = requests.get(url)
  if r.status_code == 200: return True, "OK %s" % url
  else: return False, "KO %s" % url

def check_3():
  url = urls[2]
  r = requests.get(url)
  if r.status_code == 200: return True, "OK %s" % url
  else: return False, "KO %s" % url


if len(urls)>0: health.add_check(check_1) 
if len(urls)>1: health.add_check(check_2) 
if len(urls)>2: health.add_check(check_3) 


#@app.route("/")
#def root():
#  return "Hello World!"

