from pf import app
from pf import dbfunc as db
from pf import jwtdecodenoverify as jwtnoverify
#from order import dbfunc as db
#from order import jwtdecodenoverify as jwtnoverify


#from order import app
from flask import request, make_response, jsonify, Response, redirect
from dateutil import tz
from datetime import datetime, timedelta
from datetime import date
from multiprocessing import Process
from multiprocessing import Pool
from pf import mforderapi
from pf import mfsiporder
import requests
from pf import webapp_settings

import psycopg2
import json
import jwt
import time

#@app.route('/',methods=['POST','GET','OPTIONS'])
def test_home():
  print("inside home route")
  return("welcome mr nat")
