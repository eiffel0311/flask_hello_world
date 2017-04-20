#!/usr/bin/env python
# coding=utf-8

from flask import jsonify
from app.api import api
from app import db
from app.models.meta_db import MetaDatasource

@api.route('/hello_world', methods=['GET'])
def hello_world():
    [meta_datasource.name for meta_datasource in db.session.query(MetaDatasource)]
    data = {
        'code': 200,
        'msg': '',
        'data': [meta_datasource.name for meta_datasource in db.session.query(MetaDatasource)]
    }
    return jsonify(data), 200