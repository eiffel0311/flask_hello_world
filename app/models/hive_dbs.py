#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db

class HiveDbs(db.Model):
    __tablename__ = 'hivedbs'
    id = db.Column(db.Integer, primary_key=True)
    dbname = db.Column(db.Text())
    dbdesc = db.Column(db.Text())
    layer = db.Column(db.Text())
    dictname = db.Column(db.Text())
    owner = db.Column(db.Text())
    pdbname = db.Column(db.Text())
    grantuser = db.Column(db.Text())
    creator = db.Column(db.Text())
    modifier = db.Column(db.Text())
    createtime = db.Column(db.Text())
    modifytime = db.Column(db.Text())

    @staticmethod
    def from_json(hive_db_json):
        dbname = hive_db_json.get('name')
        dbdesc = hive_db_json.get('intro')
        layer = hive_db_json.get('layer')

        owner = hive_db_json.get('owner')
        pdbname = hive_db_json.get('mapedb')
        grantuser = hive_db_json.get('granted')
        creator = hive_db_json.get('creator')
        modifier = hive_db_json.get('modifier')
        createtime = hive_db_json.get('createtime')
        modifytime = hive_db_json.get('createtime')

        return HiveDbs(
            dbname=dbname,
            dbdesc=dbdesc,
            layer=layer,

            owner=owner,
            pdbname=pdbname,
            grantuser=grantuser,
            creator=creator,
            modifier=modifier,
            createtime=createtime,
            modifytime=modifytime
        )