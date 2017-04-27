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


#------------------------------tables--------------------------------------
@api.route('/tables/<int:id>', methods = ['GET'])
def tables_show(id = None):
    """
    展示一个表的详情
    :param id:
    :return:
    """
    mytable = db.session.query(HiveTbls).filter(HiveTbls.id == id).first()
    if mytable is None:
        data = {
            'code' : 201,
            'msg': 'table not exist'
        }
        return jsonify(data), 201
    else:
        data = {
            'code': 200,
            'msg': '',
            'data': {
                'id': mytable.id,
                'bsline': mytable.bsline,
                'src_name': mytable.src_name,
                'topic': mytable.topic,
                'db_name': mytable.dbname,
                'table_name': mytable.tblname,
                'table_name_cn': mytable.tblnamecn,
                'desc': mytable.desc,
                'file_format': mytable.fileformat,
                'record_format': mytable.recordformat,
                'collection_terminator': mytable.collection_terminator,
                'field_terminator': mytable.field_terminator,
                'map_key_terminator': mytable.map_key_terminator,
                'period': mytable.period,
                'status': mytable.status,
                'rows': mytable.rows,
                'space': mytable.space,
                'creator': mytable.creator,
                'modifier': mytable.modifier,
                'create_time': mytable.createtime,
                'modify_time': mytable.modifytime
            }
        }
        return jsonify(data), 200


@api.route('/table_schema', methods=['GET'])
def table_schema():
    """
    获取某个表的结构
    :param id:数据库名字, 表的名字
    :return:
    """
    db_name = request.args.get('db_name')
    table_name = request.args.get('table_name')
    data = {
        'code': 200,
        'msg': '',
        'data': [
                  {
                      'field_seq': meta_datasource.seq,
                      'field_name_des': meta_datasource.namecn,
                      'field_name': meta_datasource.tblname,
                      'field_type': meta_datasource.type
                  } for meta_datasource in db.session.query(HiveFlds).filter(and_(HiveFlds.dbname == db_name, HiveFlds.tblname == table_name))]
    }
    return jsonify(data), 200

@api.route('/search_tables', methods = ['GET'])
def search_tables():
    """
    根据数据库名搜索表的详情
    :return:
    """
    db_name = request.args.get('db_name')
    data = {
        'code': 200,
        'msg': '',
        'data': [
            {
                'id': meta_datasource.id,
                'table_name_en': meta_datasource.tblname,
                'table_name_ch': meta_datasource.tblnamecn,
                'topic': meta_datasource.topic,
                'business_line': meta_datasource.bsline,
                'compute_period': meta_datasource.period,
                'status': meta_datasource.status,
                'creator': meta_datasource.creator
            } for meta_datasource in db.session.query(HiveTbls).filter(HiveTbls.dbname == db_name)
        ]
    }
    return jsonify(data), 200


@api.route('/tables/<int:id>', methods = ['DELETE'])
def table_delete(id = None):
    """
    根据表的ID删除表的数据
    :return:
    """
    # 删除表的记录
    table = db.session.query(HiveTbls).filter_by(id=id).first()

    if table is None:
        data = {
            'code': 201,
            'msg': 'table not exist'
        }
        return jsonify(data), 201
    else:
        db_name = table.dbname
        table_name = table.tblname
        db.session.delete(table)

        # 删除表相关字段的记录
        db.session.query(HiveFlds).filter(and_(HiveFlds.dbname == db_name, HiveFlds.tblname == table_name)).delete()
        db.session.commit()
        data = {
            'code': 200,
            'msg': ''
        }
        return jsonify(data), 200

@api.route('/tables/new', methods=['POST'])
def tables_new():
    """
    新建一个表
    """

    return "hello"

#--------------------------------------------------------------------------