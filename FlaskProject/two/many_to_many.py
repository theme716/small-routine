from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskweb"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# 绑定app至SQLAlchemy
db = SQLAlchemy(app)



# tags:和relationship里面的secondary参数的值保持对应关系
# post_tag：这是中间表的表名
# 括号里面是两个字段
tags = db.Table('manytomany_post_tag',  # 中间表：
    # tag_id:字段名
    # db.Integer:字段类型
    # db.ForeignKey：外键
    db.Column('tag_id', db.Integer, db.ForeignKey('manytomany_tags.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('manytomany_posts.id'))
)
class Posts(db.Model): #文章
    __tablename__ = 'manytomany_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    # 参数：Tage:和这个模型产生关系的模型的类名，
    #        secondary:和中间表=左边的变量保持对应关系就可以了
    #       backref:反向给和它产生关系的表
    tags = db.relationship('Tags',secondary=tags,backref='Posts')
class Tags(db.Model): #标签
    __tablename__ = 'manytomany_tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # def __repr__(self):
    #     return self.name

if __name__ == '__main__':
    # db.create_all()

    # 增
    # 创建文章
    # p1 = Posts(title='flask开发')
    # p2 = Posts(title='django开发')
    # p3 = Posts(title='web框架开发博客')
    # # 创建标签
    # t1 = Tags(name='falsk')
    # t2 = Tags(name='django')
    # t3 = Tags(name='web框架')
    #
    # # 给文章添加标签的同时会创建标签
    # p1.tags = [t1,t3] #这里的tags是Posts模型类里面的tags字段
    # p2.tags = [t2,t3]
    # p3.tags = [t3]
    #
    # db.session.add(p1)
    # db.session.add(p2)
    # db.session.add(p3)
    # db.session.commit()

    # 单独创建一个标签
    # t4 = Tags(name='Linux')
    # db.session.add(t4)
    # db.session.commit()

    # 单独为一篇文章添加标签
        # p3 = Posts.query.filter_by(title='web框架开发博客').first()  # XXX
        # t4 = Tags.query.filter_by(name='Linux').first()
        # p3.tags += [t4]
        # db.session.add(p3)
        # db.session.commit()

    # 查
    # 根据文章查标签
        # (查询第一篇文章的)
            # p = db.session.query(Posts).first()
            # print(p)
            # print(p.title)
            # print(p.tags)
        # （查询所有文章的）
            # p = db.session.query(Posts).all()
            # for i in p:
            #     # print(i.title,i.tags)
            #     # flask开发 [<Tags 1>, <Tags 2>]
            #     # django开发 [<Tags 2>, <Tags 3>]
            #     # web框架开发博客 [<Tags 2>, <Tags 4>]
            #     tagname = ''
            #     for x in i.tags:
            #         tagname += x.name
            #         tagname += '/'
            #     print(i.title + ':' + tagname)
            #     # flask开发: falsk / web框架 /
            #     # django开发: web框架 / django /
            #     # web框架开发博客: web框架 / Linux /

    # 根据标签查文章
        # t = db.session.query(Tags).get(2)
        # print(t)
        # print(t.name)
        # print(t.Posts)
        # #<Tags 1>
        # # falsk
        # # [<Posts 1>, <Posts 2>, <Posts 3>]

    # 删
        # 当删除一篇文章的时候，关系表中对应的关系数据也会被删掉
            # p = Posts.query.get(1)
            # db.session.delete(p)
            # db.session.commit()
        # 当删除一个标签的时候，关系表中对应的关系数据也会被删掉
            # t = Tags.query.get(3)
            # db.session.delete(t)
            # db.session.commit()
    # 改

    pass
