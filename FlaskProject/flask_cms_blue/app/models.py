from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime,hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost/flask_cms_blue"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


#会员数据模型
class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    pwd= db.Column(db.String(100))
    email= db.Column(db.String(100))
    phone= db.Column(db.String(11))
    face = db.Column(db.String(255),default='user.jpg')
    # 1 正常,2,禁用
    status = db.Column(db.Integer,default=1)
    addtime = db.Column(db.DateTime,index=True,default=datetime.datetime.now)

    def md5password(self,pwd):
        # 创建md5对象
        hl = hashlib.md5()
        # 执行md5加密
        hl.update(pwd.encode(encoding='utf-8'))
        # 获取加密后的密文
        return hl.hexdigest()
    # 密文判断
    def checkpassword(self, pwd):
        if self.md5password(pwd) == self.pwd:
            return True
        else:
            return False

# 分类
class Types(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(50),index=True)
    pid = db.Column(db.Integer)


# 博文
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True)
    context = db.Column(db.Text)
    type_id = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    # 1 正常,2,禁用
    status = db.Column(db.Integer, default=1)
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)


# 标签
class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, index=True)
    tagname = db.Column(db.String(50), index=True)


# 文章和标签的关系
class Ats(db.Model):
    __tablename__ = 'ats'
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer)
    tags_id = db.Column(db.Integer)


if __name__ == '__main__':
    db.create_all()
