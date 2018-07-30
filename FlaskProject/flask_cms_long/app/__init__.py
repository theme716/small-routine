# 注册蓝图
from flask import render_template
import os
from app.models import app

app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
# url_prefix = '/admin'---指定前缀
# 如果完整路径是/admin/user/list/   那么路由里面就不用写/admin了，直接写后面剩下的
app.register_blueprint(admin_blueprint,url_prefix='/admin/')

app.secret_key = os.urandom(20)
# 配置项目根路径
app.config['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__)) #C:\Users\ck-pc\Documents\FlaskProject\flask_cms_long\app
# 配置项目上传文件路径
app.config['uploads'] = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static/uploads/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
