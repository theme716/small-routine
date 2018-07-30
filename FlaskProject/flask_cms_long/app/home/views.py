from flask import render_template,flash,redirect,session,Response,request,url_for
from . import home
from app.home.form import RegisterForm,LoginForm,ArticleAddFrom
from app.home.captcha import Captcha
from app.models import db,Users,Articles
from werkzeug.security import generate_password_hash
import os,uuid
from app import app
from functools import wraps

def login_req(f):
    @wraps(f)
    def req(*args,**kwargs):
        if 'account' in session:
            return f(*args,**kwargs)
        else:
            return "<script>alert('请登录');location.href='/login/'</script>"
    return req


@home.route('/')
def index():
    return '这是前台首页'

# 登录
@home.route('/login/',methods=['GET','POST'])
def login():
    fom = LoginForm()
    if fom.validate_on_submit():
        # 获取提交的数据
        data = fom.data
        # 在session中存储用户名
        session['account'] = data['account']
        flash('登录成功',category='login')
        return redirect(url_for('home.art_list',name=session['account']))
    return render_template('home/login.html',title='登录',form=fom)

# 退出登录
@home.route('/logout/')
def logout():
    session.pop('account')
    return redirect(url_for('home.login'))

# 注册
@home.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 获取用户输入
        data = form.data
        user = Users(
            account=data['account'],
            # 加盐加密
            pwd= generate_password_hash(data['pwd'])
        )
        db.session.add(user)
        db.session.commit()
        # 一闪消息
        flash('注册成功，请登录')
        return redirect('/login/')

    return render_template('home/register.html',title='注册',form=form)

# 生成验证码
@home.route('/captcha/')
def captcha_my():
    c = Captcha()
    info = c.create_captcha()
    image = os.path.join(
        app.config['BASE_DIR'],
        "static/captcha/")+info['image_name']
    # 读取验证码
    with open(image,'rb') as f:
        image = f.read()
    # 获取验证码具体字母和数字
    session['captcha'] = info['captcha']
    return Response(image,mimetype='jpeg')

# 添加文章
@home.route('/art/add/',methods=['GET','POST'])
@login_req
def art_add():
    rul = str(request.url_rule)
    if rul[5:7] == 'li':
        rul = 'list'
    form=ArticleAddFrom()
    if form.validate_on_submit():
        data = form.data
        if data['logo']:
            # 保存上传的封面
            # 获取文件名
            file = form.logo.data.filename
            # 起一个文件名
            file = str(uuid.uuid4()) + os.path.splitext(file)[-1]
            # 查看有没有保存上传文件的目录，如果没有则自动新建
            up_dir = os.path.join(app.config['BASE_DIR'], 'static/uploads/')
            if not os.path.exists(up_dir):
                os.makedirs(up_dir)
            # 存储文件
            form.logo.data.save(up_dir + file)
        else:
            file = ''

        # 在文章数据库中写入数据
        art = Articles()
        art.title = data['title']
        art.category = data['category']
        # 获取用户的id
        user = Users.query.filter_by(account=session['account']).first()
        art.uid=user.id
        art.content = data['content']
        art.logo = file
        db.session.add(art)
        db.session.commit()
        return redirect(url_for('home.art_list'))
    return render_template('home/art_add.html',title=session['account']+'的博客',rul=rul,form=form)

# 文章列表
@home.route('/art/list/')
@login_req
def art_list():
    rul = str(request.url_rule)
    if rul[5:7] == 'li':
        rul = 'list'
    # 查询 该作者的所有文章
    user = Users.query.filter_by(account=session['account']).first()
    articles = Articles.query.filter_by(uid=user.id).order_by(Articles.add_time.desc()).all()

    return render_template('home/art_list.html',title=session['account']+'的博客',rul=rul,articles=articles)


# 删除文章
@home.route('/art/del/<id>/')
@login_req
def art_del(id):
    article = Articles.query.get_or_404(id)
    logo = article.logo
    if logo:
        url = os.path.join(app.config['BASE_DIR'],'static/uploads/')
        os.remove(url+logo)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('home.art_list'))

# 文章详情
@home.route('/art/info/<id>/')
def art_info(id):
    article = Articles.query.get_or_404(id)
    typelist = [(1,'php'),(2,'java'),(3,'python'),(4,'C')]
    type = typelist[article.category-1][1]
    return render_template('home/art_info.html',article=article,type=type)


# 编辑文章
@home.route('/art/edit/<id>/')
@login_req
def art_edit(id):
    article = Articles.query.get_or_404(id)
    return render_template('home/art_edit.html',article=article)




