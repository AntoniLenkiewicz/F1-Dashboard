import sys
import time
from datetime import datetime, timezone
from flask import Flask
import fastf1

sys.path.insert(1, 'controllers')
from controllers import routes


fastf1.Cache.enable_cache("./cache")


app = Flask(__name__)

routes(app)

