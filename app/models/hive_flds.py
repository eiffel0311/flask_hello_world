#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db

class HiveFlds(db.Model):
    __tablename__ = 'hiveflds'
    id = db.Column(db.Integer, primary_key=True)
    dbname = db.Column(db.Text())
    tblname = db.Column(db.Text())
    seq = db.Column(db.Integer)
    namecn = db.Column(db.Text())
    name = db.Column(db.Text())
    type = db.Column(db.Text())
    pk = db.Column(db.Text())
    part = db.Column(db.Text())
    comment = db.Column(db.Text())
    creator = db.Column(db.Text())
    modifier = db.Column(db.Text())
    createtime = db.Column(db.Text())
    modifytime = db.Column(db.Text())