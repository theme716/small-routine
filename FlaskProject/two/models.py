from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskweb"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# 绑定app至SQLAlchemy
db = SQLAlchemy(app)


# 定义会员模型
class Users(db.Model):
    # 指定表名
    __tablename__ = 'users1'

    # 指定属性(字段)
    id = db.Column(db.Integer,primary_key=True)
    uname = db.Column(db.String(100),unique=True)
    upass = db.Column(db.String(100))
    email = db.Column(db.String(100))
    pic = db.Column(db.String(100),default='user.jpg')
    addtime = db.Column(db.DateTime,default=datetime.datetime.now)

    def __init__(self,uname=None,upass=None,email=None):
        self.uname = uname
        self.upass = upass
        self.email = email

    # 此处__str__不能用
    def __repr__(self):
        return self.uname



if __name__ == '__main__':
    # 创建所有的模型
    # db.create_all()
    # 删除上面的模型对应的表（只认表名）
    # db.drop_all()

    # 增
        # # 方法1：普通方法
        # u = Users()
        # u.uname = '科技化工'
        # u.upass = '123456'
        # u.email = 'sssss'
        # # 添加数据对象
        # db.session.add(u) #session 有会话的意思
        # # 提交数据对象
        # db.session.commit()

        # 方法2：
        # u = Users('a','b','c')
        # db.session.add(u)
        # db.session.commit()

        # 方法三
        # u = Users(
        #     uname = 'dsdfsf',
        #     upass = 'ccc',
        # )
        # db.session.add(u)
        # db.session.commit()

    # 删
        # 获取对象
        # u = Users.query.get(3)
        # # 执行删除
        # db.session.delete(u)
        # db.session.commit()


    # 改
        # u = Users.query.get(4)
        # u.uname = '李四'
        # db.session.add(u)
        # db.session.commit()


    # 查

    # 总结 ：基本方法get() all() first()
            # 高级方法
                    # 按照字段查询：filter_by().first() filter_by().all()
                    # 复杂查询：filter(模型名.字段名.endswith()/startswith()).all()
                    # 排序，并查询所有： order_by(模型名.字段名) order_by(模型名.字段名.desc())---倒序
                    # 限制返回数量:limit().all()   limit().first()   offset().limit()
                    # 跳过几条：offset()......
                    # 统计查询到几条：count()


        # # 1.get方法，只能对于主键使用，只返回一个，如果查询不到，返回None
        # u = Users.query.get(4)
        # print(u)

        # # 2.get_or_404() 方法,只返回一个数据对象，如果查询不到，返回一个404错误
        # u = Users.query.get_or_404(2)
        # print(u)

        # # 3. all() 方法 first()
        # us = Users.query.all()
        # print(us)
        # us = Users.query.first()
        # print(us)


        # # 4. filter_by()方法:后面跟all()  first()，如果没有找到返回[],或者None
        # u = Users.query.filter_by(uname='莱斯特').all()
        # print(u)
        # u = Users.query.filter_by(uname='list').first()
        # print(u)


        # # 5. filter() 方法
        # # Users.uname.endswith() Users模型的uname字段，以什么什么结尾
        # u = Users.query.filter(Users.uname.endswith('/')).all()
        # print(u)
        # # startswith()以什么开头
        # u = Users.query.filter(Users.uname.startswith('/')).all()
        # print(u)

        # # 6. order_by()方法，查询所有并排序
        # # 正序
        # u = Users.query.order_by(Users.id)
        # for i in u:
        #     print(i)
        # # 倒序
        # u = Users.query.order_by(Users.id.desc())
        # for i in u:
        #     print(i)

        # # 7. limit() 限制返数据的数量
        # u = Users.query.limit(5).all()
        # print(u)
        # # 跳过一个
        # u = Users.query.offset(1).limit(5).all()
        # print(u)

        # # 8. offset() 跳过几条
        # u = Users.query.offset(1).all()
        # print(u)
        # 这个顺序不能乱
        # u = Users.query.filter(Users.uname.endswith('5')).offset(1).limit(1).all()
        # print(u)

        # # 9.count() 返回几条
        # u = Users.query.count()
        # u = Users.query.filter(Users.uname.endswith('5')).count()
        # print(u)

    pass

