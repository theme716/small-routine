from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskweb"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# 绑定app至SQLAlchemy
db = SQLAlchemy(app)

# 通过用户查详情的时候，使用userinfo字段
# 通过用户详情查用户的时候，使用userinfo.users.uname...这样的方式
class User(db.Model):
    __tablename__ = 'onetoone_users'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(50))
    # relationship()
    # 第一个参数是产生关系的类，即UserInfo;
    # backref：反向给和它产生关系的表，userinfo查user的时候用。
    # uselist:默认True,如果设置成False,则只能存在一个关系对应的数据
    userinfo = db.relationship('UserInfo', backref='users', cascade="all, delete,delete-orphan",uselist=False)
    def __repr__(self):
        return self.uname

class UserInfo(db.Model):
    __tablename__ = 'onetoone_userinfo'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    # 这就是一个单纯的数字，而不是一个对象,如果这里不用unique 唯一索引加以限制，那一个user可以有多个userinfo，即不是一对一关系了
    users_id = db.Column(db.Integer, db.ForeignKey('onetoone_users.id'),unique=True)
    def __repr__(self):
        return str(self.users_id)

if __name__ == '__main__':
    # db.create_all()

    # 增

        # 注意：
            # 1、这两个表的数据可以分开添加，即添加完一个再添加另一个
            # 2、i.user_id = u.id 或者 i.user_id = 1这两种写法都可以，但是直接数字写法必须是user表中存在的id

        # u = User()
        # u.uname = '张三'
        # db.session.add(u)
        # db.session.commit()
        #
        # i = UserInfo()
        # i.email = '@qq'
        # # 这里是一个数字就够了，而不用是一个对象，这是与Django不同的地方
        # i.users_id = u.id
        # db.session.add(i)
        # db.session.commit()

    # 删
        # 由于relationship存在于user模型中，删除User中的一条数据会删除其对应的UserInfo表中的数据
        # u = User.query.get(1)
        # db.session.delete(u)
        # db.session.commit()
        # 由于relationship存在于user模型中，删除UserInfo中的一条数据不会删除User中对应的数据
        # u = UserInfo.query.get(1)     # X
        # db.session.delete(u)
        # db.session.commit()

    # 查
        # 通过User表查UserInfo
            # u = User.query.get(1)
            # uinfo = u.userinfo #此处的userinfo是User模型中的userinfo字段
            # print(uinfo)
            # print(uinfo.email)
        # 通过UserInfo查User
            # i = UserInfo.query.get(1)
            # u = i.users #此处的users是User模型中userinfo字段的backref参数
            # print(i)
            # print(u)

    # 改
        # 通过User查到UserInfo 并 修改UserInfo
            # u = User.query.get(1)
            # i = u.userinfo
            # i.email = 'xin@qq.com'
            # db.session.add(i)
            # db.session.commit()
        # 通过UserInfo查到User并修改
            # i = UserInfo.query.get(1)
            # u = i.users
            # u.uname = 'newname'
            # db.session.add(u)
            # db.session.commit()

    pass