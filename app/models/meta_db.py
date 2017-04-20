#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db

class MetaDatasource(db.Model):
    """
    数据
    """
    __tablename__ = 'meta_datasource'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    source = db.Column(db.Text())
    contacts_inner_name = db.Column(db.Text())
    contacts_outer_name = db.Column(db.Text())
    contacts_outer_phone = db.Column(db.Text())