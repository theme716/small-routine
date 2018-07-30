from . import home

@home.route('/')
def index():
    return 'home_index'


@home.route('/admin/aa/')
def ad():
    return 'ad'