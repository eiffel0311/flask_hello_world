#!/usr/bin/env python
# coding=utf-8

from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
app = Flask(__name__)
# db.app = app
# db.init_app(app)
from app.api import api as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')

app.run()