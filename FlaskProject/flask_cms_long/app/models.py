from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/flask_cms_my?charset=utf8"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True)
    account = db.Column(db.String(20),nullable=False)
    pwd = db.Column(db.String(100),nullable=False)
    add_time = db.Column(db.DATETIME,default=datetime.now)
    arts = db.relationship('Articles',backref="users",cascade="all, delete,delete-orphan")

    def check_pwd(self,pwd):
        return check_password_hash(self.pwd,pwd)

class Articles(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    # 类别
    category = db.Column(db.INTEGER,nullable=True)
    # 外键
    uid = db.Column(db.INTEGER,db.ForeignKey('users.id'))
    logo = db.Column(db.String(100),nullable=True)
    content = db.Column(db.Text,nullable=False)
    add_time = db.Column(db.DATETIME,default=datetime.now,nullable=True)
    def __repr__(self):
        return self.title
if __name__=='__main__':
    db.create_all()