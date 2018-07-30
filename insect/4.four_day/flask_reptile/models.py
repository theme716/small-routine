from flask_sqlalchemy import SQLAlchemy
from flask_reptile import app

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost/reptile"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer,primary_key=True)
    newtime = db.Column(db.String(50),unique=True)
    newcontent = db.Column(db.Text)

class Friends(db.Model):
    __tablename__ = 'friends'
    id = db.Column(db.Integer,primary_key=True)
    UserName = db.Column(db.String(255),unique=True)
    NickName = db.Column(db.String(100))

if __name__ == '__main__':
    db.create_all()
