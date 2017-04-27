#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db

class HiveTbls(db.Model):
    __tablename__ = 'hivetbls'
    id = db.Column(db.Integer, primary_key=True)
    bsline = db.Column(db.Text())
    src_name = db.Column(db.Text())
    topic = db.Column(db.Text())
    dbname = db.Column(db.Text())
    tblname = db.Column(db.Text())
    tblnamecn = db.Column(db.Text())
    desc = db.Column(db.Text())
    fileformat = db.Column(db.Text())
    recordformat = db.Column(db.Text())
    collection_terminator = db.Column(db.Text())
    field_terminator = db.Column(db.Text())
    map_key_terminator = db.Column(db.Text())
    period = db.Column(db.Text())
    status = db.Column(db.Text())
    rows = db.Column(db.Integer)
    space = db.Column(db.Integer)
    creator = db.Column(db.Text())
    modifier = db.Column(db.Text())
    createtime = db.Column(db.Text())
    modifytime = db.Column(db.Text())