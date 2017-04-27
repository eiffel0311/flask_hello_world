#!/usr/bin/env python
# coding=utf-8

from flask import jsonify
from flask import request
from app.api import api
from app import db
from app.models.data_src import DataSrc
from app.models.hive_tbls import HiveTbls
from app.models.hive_flds import HiveFlds
from app.models.hive_dbs import HiveDbs
from sqlalchemy import and_
import datetime


@api.route('/meta_db_datasource', methods=['GET'])
def meta_db_datasource():
    """
    获取所有的数据源
    :return:
    """
    data = {
        'code': 200,
        'msg': '',
        'data': [{'id': meta_datasource.id, 'name': meta_datasource.name} for meta_datasource in db.session.query(DataSrc)]
    }
    return jsonify(data), 200


@api.route('/datasources/<int:id>', methods=['GET'])
def datasource_tables(id = None):
    """
    获取某个数据数据源下面的所有的表
    :param id:数据源ID
    :return:
    """
    data = {
        'code': 200,
        'msg': '',
        'data': [
                   {
                       'id': meta_datasource.id,
                       'db_name': meta_datasource.dbname,
                       'table_name': meta_datasource.tblname
                   } for meta_datasource in db.session.query(HiveTbls).filter_by(src_name = db.session.query(DataSrc).filter_by(id=id).first().name)]
    }
    return jsonify(data), 200
