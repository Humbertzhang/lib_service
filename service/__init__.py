# -*- coding: utf-8 -*-
import logging
from flask import Flask

app = Flask(__name__)

# Gunicorn Error Logger
gel = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gel.handlers)
app.logger.setLevel(logging.DEBUG)

from api import api
app.register_blueprint(api, url_prefix='/api')
