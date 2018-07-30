from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app连接数据库的配置
# root:账户 1234567:密码  127.0.0.1:3306数据库地址和端口  flaskweb 数据库名称
# 必须要在环境中下载好pymysql
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flaskweb'
# 如果设置成True(默认情况),Flask-SQLALchemy将会最终对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


# 创建连接：
db = SQLAlchemy(app)

class User(db.Model):
    # 表名(默认表名是小写类名)
    __tablename__ = 'user'
    # 主键，自增(必须自定义主键，如果不自定义，不会像Django一样自动生成)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    # 唯一索引
    name = db.Column(db.String(30),unique=True,nullable=False)
    # 不允许为空
    password = db.Column(db.String(100),nullable=False)
    # 允许为空（默认）
    email = db.Column(db.String(100),nullable=True)
    phone = db.Column(db.String(11))
    # 大文本
    info = db.Column(db.Text)
    pic = db.Column(db.String(255))
    # 默认值
    addtime = db.Column(db.DateTime,default=datetime.now)

    def __repr__(self):
        return self.name

if __name__ == '__main__':
    # 建表
    db.create_all()