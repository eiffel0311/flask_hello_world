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



#------------------------------dbs------------------------------------------
@api.route('/get_dbs', methods=['GET'])
def get_dbs():
    """
　　获取所有的数据库, 按层分组
    :return:
    """
    data = {
        'code': 200,
        'msg': '',
        'data': {
            'T1': [{'id': meta_datasource.id, 'db_name': meta_datasource.dbname} for meta_datasource in db.session.query(HiveDbs).filter(HiveDbs.layer == 'T1')],
            'T2': [{'id': meta_datasource.id, 'db_name': meta_datasource.dbname} for meta_datasource in db.session.query(HiveDbs).filter(HiveDbs.layer == 'T2')],
            'T3': [{'id': meta_datasource.id, 'db_name': meta_datasource.dbname} for meta_datasource in db.session.query(HiveDbs).filter(HiveDbs.layer == 'T3')],
            'TP': [{'id': meta_datasource.id, 'db_name': meta_datasource.dbname} for meta_datasource in db.session.query(HiveDbs).filter(HiveDbs.layer == 'TP')]
        }
    }
    return jsonify(data), 200

@api.route('/dbs/<int:id>', methods = ['GET'])
def dbs_show(id = None):
    """
    展示一个数据库的详情
    :param id:
    :return:
    """
    mydb = db.session.query(HiveDbs).filter(HiveDbs.id == id).first()
    if mydb is None:
        data = {
            'code' : 201,
            'msg': 'db not exist'
        }
        return jsonify(data), 201
    else:
        data = {
            'code': 200,
            'msg': '',
            'data': {
                'id': mydb.id,
                'db_name': mydb.dbname,
                'db_desc': mydb.dbdesc,
                'layer': mydb.layer,
                'dict_name': mydb.dictname,
                'owner': mydb.owner,
                'pdb_name': mydb.pdbname,
                'grantuser': mydb.grantuser,
                'creator': mydb.creator,
                'modifier': mydb.modifier,
                'create_time': mydb.createtime,
                'modify_time': mydb.modifytime
            }
        }
        return jsonify(data), 200

@api.route('/dbs/new', methods = ['POST'])
def dbs_new():
    """
    新建数据库
    :return:
    """
    db_name = request.json.get('name')
    if db.session.query(HiveDbs).filter(HiveDbs.dbname == db_name).first() is None:
        mydb = HiveDbs.from_json(request.json)
        db.session.add(mydb)
        db.session.commit()
        data = {
            'code': 200,
            'msg': ''
        }
        return jsonify(data), 200
    else:
        data = {
            'code' : 201,
            'msg': 'db exist'
        }
        return jsonify(data), 201

@api.route('/dbs/update', methods=['POST'])
def dbs_update():
    """
    根据数据库的名字修改数据的属性
    :return:
    """
    request_data = request.json
    db_name = request_data.get('name')
    db_desc = request_data.get('intro')
    layer = request_data.get('layer')
    modifier = request_data.get('modifier')
    mydb = db.session.query(HiveDbs).filter(HiveDbs.dbname == db_name).first()
    if mydb is None:
        data = {
            'code' : 201,
            'msg': 'db not exist'
        }
        return jsonify(data), 201
    else:
        mydb.dbdesc = db_desc
        mydb.layer = layer
        mydb.modifier = modifier
        mydb.modifytime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.add(mydb)
        db.session.commit()
        data = {
            'code': 200,
            'msg': ''
        }
        return jsonify(data), 200

@api.route('/dbs/delete/<string:db_name>', methods=['DELETE'])
def dbs_delete(db_name):
    """
    根据数据库的名字删除数据库
    :return:
    """
    mydb = db.session.query(HiveDbs).filter(HiveDbs.dbname == db_name).first()
    if mydb is None:
        data = {
            'code': 201,
            'mdg': 'db not exist'
        }
        return jsonify(data), 201
    else:
        # 删除数据库记录
        db.session.delete(mydb)
        # 删除表记录
        db.session.query(HiveTbls).filter(HiveTbls.dbname == db_name).delete()
        #  删除字段记录
        db.session.query(HiveFlds).filter(HiveFlds.dbname == db_name).delete()
        db.session.commit()
        data = {
            'code' : 200,
            'msg': ''
        }
        return jsonify(data), 200


