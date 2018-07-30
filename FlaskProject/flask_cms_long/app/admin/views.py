from . import admin

@admin.route('/')
def index():

    return '这是后台首页'