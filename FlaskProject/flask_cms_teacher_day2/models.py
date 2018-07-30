from werkzeug.security import check_password_hash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from datetime import timedelta


app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(20)

# 配置项目根路径
app.config['BASE_DIR'] = os.path.dirname(__file__)

# 配置上传路径
app.config['uploads'] = os.path.join(os.path.dirname(__file__),'uploads/')

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/flask_cms_teacher?charset=utf8"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

app.permanent_session_lifetime = timedelta(hours=1)

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'py09_cms_user'
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True)
    account = db.Column(db.String(20),nullable=False)
    pwd = db.Column(db.String(100),nullable=False)
    add_time = db.Column(db.DATETIME,default=datetime.now)
    arts = db.relationship('Article',backref="user",cascade="all, delete,delete-orphan")

    def __repr__(self):
        return self.account

    # 检查密码是否正确
    def check_pwd(self,pwd):
        # 返回True，密码正确   返回false 密码错误
        return check_password_hash(self.pwd,pwd)

class Article(db.Model):
    __tablename__ = 'py09_cms_article'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    category = db.Column(db.INTEGER,nullable=True)
    # 外键
    uid = db.Column(db.INTEGER,db.ForeignKey('py09_cms_user.id'))
    logo = db.Column(db.String(100),nullable=True)
    content = db.Column(db.Text,nullable=False)
    add_time = db.Column(db.DATETIME,default=datetime.now,nullable=True)

    def __repr__(self):
        return self.title


if __name__ == '__main__':
    db.create_all()