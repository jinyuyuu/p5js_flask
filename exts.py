# 这个文件的意义就是解决循环引用的情况,放插件的

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
