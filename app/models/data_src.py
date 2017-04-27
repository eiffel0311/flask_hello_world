#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db

class DataSrc(db.Model):
    __tablename__ = 'datasrc'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    abname = db.Column(db.Text())
    src_contact = db.Column(db.Text())
    access_man = db.Column(db.Text())
    creator = db.Column(db.Text())
    modifier = db.Column(db.Text())
    createtime = db.Column(db.Text())
    modifytime = db.Column(db.Text())