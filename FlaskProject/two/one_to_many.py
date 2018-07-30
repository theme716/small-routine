from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskweb"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# 绑定app至SQLAlchemy
db = SQLAlchemy(app)

# 班级 1
class Classs(db.Model):
    __tablename__ = 'onetomore_class'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(50))
    # stus = db.relationship('Stus',backref="classs")
    stus = db.relationship('Stus',backref="classs",cascade="all,delete,delete-orphan")
    # def __repr__(self):
    #     return self.cname
# 学员 多
class Stus(db.Model):
    __tablename__ = 'onetomore_stu'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(50))
    c_id = db.Column(db.Integer, db.ForeignKey('onetomore_class.id'))
    # def __repr__(self):
    #     return self.uname

if __name__ == '__main__':
    db.create_all()

    # 增

        # c1 = Classs(cname='py1')
        # c2 = Classs(cname='py2')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        #
        # s1 = Stus(uname='张1',c_id=c1.id)
        # s2 = Stus(uname='张2',c_id=c1.id)
        # s3 = Stus(uname='张3',c_id=c1.id)
        # s4 = Stus(uname='张4',c_id=c2.id)
        # s5 = Stus(uname='张5',c_id=c2.id)
        # s6 = Stus(uname='张6',c_id=c2.id)
        # db.session.add(s1)
        # db.session.add(s2)
        # db.session.add(s3)
        # db.session.add(s4)
        # db.session.add(s5)
        # db.session.add(s6)
        # db.session.commit()

    # 删

    # 改

    # 查
    # 根据班级查询所有学员
        # c = Classs.query.get(1)
        # s = c.stus  #这个stus是Classs里面的一个字段
        # # [<Stus 1>, <Stus 2>, <Stus 3>]
        # print(s)
    # 根据学员查询班级
        # s = Stus.query.get(1)
        # c = s.classs #这里的classs是Classs模型中的suts字段的backref参数
        # print(c)
    # 查询所有有班级对应的学员信息

        # 结论:
            # 1、方法1 和 方法2 Stus.query.join(Classs) 和 Classs.query.join(Stus)的结果不同，哪个模型写在前面，以哪个模型为主
            # 2、方法3 和 方法3 query()括号里面的顺序就是输出的元祖里面的数据对象的顺序

        # 方法1
        # s = Stus.query.join(Classs).filter(Stus.c_id == Classs.id).all()
        # # [<Stus 1>, <Stus 2>, <Stus 3>, <Stus 4>, <Stus 5>, <Stus 6>]
        # # select StuS.* from Stus inner join Classs on StuS.c_id = Classs.id
        # print(s)


        # 方法2
        # s = Classs.query.join(Stus).add_columns(Stus.id,Stus.uname,Classs.cname).filter(Stus.c_id==Classs.id).all()
        # # [(<Stus 1>, 1, '张1', 'py1'), (<Stus 2>, 2, '张2', 'py1'), (<Stus 3>, 3, '张3', 'py1'), (<Stus 4>, 4, '张4', 'py2'), (<Stus 5>, 5, '张5', 'py2'), (<Stus 6>, 6, '张6', 'py2')]
        # # select Stus,Stus.id,Stus.uname,Classs.cname from stu inner join classs on stu.c_id = classs.id
        # print(s)

        # 方法3
        # s = db.session.query(Classs,Stus).filter(Stus.c_id==Classs.id).all()
        # # [(<Classs 1>, <Stus 1>), (<Classs 1>, <Stus 2>), (<Classs 1>, <Stus 3>), (<Classs 2>, <Stus 4>), (<Classs 2>, <Stus 5>), (<Classs 2>, <Stus 6>)]
        # print(s)
        # for x in s:
        #     print(x)
        #     # 以下这两种写法一样
        #     print(x[0].cname)
        #     print(x.Classs.cname)

        # 方法4
        # s = db.session.query(Stus,Classs).add_columns(Stus.id,Stus.uname,Classs.cname).filter(Stus.c_id == Classs.id).all()
        # # [(<Stus 1>, <Classs 1>, 1, '张1', 'py1'), (<Stus 2>, <Classs 1>, 2, '张2', 'py1'), (<Stus 3>, <Classs 1>, 3, '张3', 'py1'), (<Stus 4>, <Classs 2>, 4, '张4', 'py2'), (<Stus 5>, <Classs 2>, 5, '张5', 'py2'), (<Stus 6>, <Classs 2>, 6, '张6', 'py2')]
        # print(s)
        # for x in s:
        #     #以下这两种写法一样
        #     print(x.Stus.uname)
        #     print(x[0].uname)