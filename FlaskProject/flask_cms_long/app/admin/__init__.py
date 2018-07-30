from flask import Blueprint
# 定义蓝图,"home"是蓝图名
admin = Blueprint("admin",__name__)

import app.admin.views