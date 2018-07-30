#### 目录结构
```
.
├── app                    ---  应用目录
│   ├── admin              ---  后台应用
│   │   ├── __init__.py   
│   │   └── views.py
│   ├── home               --- 前台应用
│   │   ├── __init__.py
│   │   └── views.py
│   ├── __init__.py        --- 初始化文件
│   ├── models.py          --- 模型文件
│   ├── static             --- 静态文件目录
│   └── templates          --- 模板目录
├── app.sql         ---  数据文件
├── manage.py       ---  入口文件
├── README.md       ---  项目说明文件
└── req.txt         ---  依赖包文件
```

#### 流程解析(自上而下)
- manage.py入口文件
```
from app import app

if __name__ == '__main__':
    app.run()


# 这里是入口文件
```
- app/\_\_init__.py 这个文件里面注册蓝图，
```
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
```
- 定义蓝图 admin/\_\_init__.py 这个文件里面定义蓝图
```
from flask import Blueprint
# 定义蓝图,"home"是蓝图名
home = Blueprint("home",__name__)

import app.home.views
```
- 视图 admin/views.py 
```
from . import admin

@admin.route('/')
def index():
    return 'admin_index'
```





