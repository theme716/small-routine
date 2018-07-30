# 注册蓝图
from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
# url_prefix = '/admin'---指定前缀
# 如果完整路径是/admin/user/list/   那么路由里面就不用写/admin了，直接写后面剩下的
app.register_blueprint(admin_blueprint,url_prefix='/admin')