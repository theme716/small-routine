from flask import Blueprint
# 定义蓝图,"home"是蓝图名
home = Blueprint("home",__name__)

import app.home.views