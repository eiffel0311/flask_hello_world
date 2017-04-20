#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.db = db


def create_app():
    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')
    return app
