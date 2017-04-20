#!/usr/bin/env python
# coding=utf-8


from flask_sqlalchemy import SQLAlchemy
import sys
from app import create_app

environment =  sys.argv[1] if len(sys.argv) == 2 else "default"  # 目前只支持两个变量：　dev, pro, 分别表示开发和生产环境

app = create_app()

if environment in ["default", "dev"]:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/root'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
elif environment == "pro":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/root'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
else:
    print "wrong params"
    sys.exit(0)

db = SQLAlchemy(app)
app.db = db


app.run(host="127.0.0.1", port="5000")