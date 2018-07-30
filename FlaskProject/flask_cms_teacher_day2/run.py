from flask import render_template,flash,redirect,Response,session,request
from models import db,app,User,Article
from forms import RegisterForm,LoginForm,ArticleAddForm,ArticleEditForm
from werkzeug.security import generate_password_hash
from captcha import Captcha
import os
import uuid
from datetime import timedelta
from functools import wraps

def login_req(f):
    @wraps(f)
    def req(*args,**kwargs):
        if 'account' in session:
            return f(*args,**kwargs)
        else:
            return redirect('/login/')
    return req

@app.route('/login/', methods=['GET','POST'])
def login():
    session.permanent = True
    form = LoginForm()
    if form.validate_on_submit():
        # 获取提交数据
        data = form.data
        # 在session中存储用户名
        session['account'] = data['account']
        flash('登录成功',category='login')

        return redirect('/art/list/1/')

    return render_template('login.html',title='登陆',form=form)

@app.route('/logout/')
def logout():
    # 从session中删除用户信息
    session.pop('account')
    return redirect('/login/')

@app.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit(): #如果数据没有问题返回True
        # 添加用户操作
        # 获取数据
        data = form.data
        user = User(
            account=data['account'],
            pwd = generate_password_hash(data['pwd'])
        )
        db.session.add(user)
        db.session.commit()
        # 一闪
        flash('注册成功，请登录')
        # 跳转到登陆页面
        return redirect('/login/')

    return render_template('register.html',title='注册',form=form)

@app.route('/art/add/',methods=['GET','POST'])
@login_req
def art_add():
    form = ArticleAddForm()
    if form.validate_on_submit():
        # 文章添加操作
        # 获取提交数据
        data = form.data
        #判断是否有文件上传
        if data['logo']: # 有文件上传、
            file = form.logo.data.filename
            logo = change_name(file)
            # 自动创建上传目录
            up_dir = os.path.join(app.config['BASE_DIR'],'static/uploads/')
            if not os.path.exists(up_dir):
                os.makedirs(up_dir)

            # 存储文件到指定目录
            form.logo.data.save(up_dir + logo)
        else:
            logo = ''
        # 把文章加入数据库里

        # 获取用户id
        user = User.query.filter_by(account=session['account']).first()
        uid = user.id

        article = Article(
            title = data['title'],
            category=data['category'],
            uid = uid,
            logo=logo,
            content=data['content'],
        )
        db.session.add(article)
        db.session.commit()
        flash('发布成功',category='article')
        return redirect('/art/list/1/')

    return render_template('art_add.html',title='添加文章',form=form)

def change_name(name):
    info = os.path.splitext(name)
    name = str(uuid.uuid4()) + info[-1]
    return name

@app.route('/art/edit/<int:id>/',methods=['GET','POST'])
@login_req
def art_edit(id):
    form = ArticleEditForm()
    article = Article.query.get_or_404(id)
    if request.method == 'GET':
        form.title.data = article.title
        form.category.data = article.category
        form.content.data = article.content

    if form.validate_on_submit():
        data = form.data
        if data['logo']: # 有文件上传、
            file = form.logo.data.filename
            logo = change_name(file)
            # 自动创建上传目录
            up_dir = os.path.join(app.config['BASE_DIR'],'static/uploads/')
            if not os.path.exists(up_dir):
                os.makedirs(up_dir)
            # 存储文件到指定目录
            form.logo.data.save(up_dir + logo)
        else:
            logo = article.logo

        article.title = data['title']
        article.category = data['category']
        article.content = data['content']
        article.logo = logo
        db.session.add(article)
        db.session.commit()
        flash('保存文章成功')

    return render_template('art_edit.html',title='编辑文章',form=form,article=article)

@app.route('/art/list/<int:page>/')
@login_req
def art_list(page):
    user = User.query.filter_by(account=session['account']).first()
    #article_list = user.arts #all().paginate(page=1,per_page=1)
    pagination = Article.query.filter_by(uid=user.id).order_by(Article.add_time.desc()).paginate(page,per_page=1)
    # print(pagination.items)
    # print(pagination.has_next) # 是否有下一页
    # print(pagination.has_prev) # 是否有上一页
    # print(pagination.iter_pages()) # 分页数字

    category = [(1,'python'),(2,'洗头'),(3,'洗澡'),(4,'洗脚')]
    return render_template('art_list.html',title='文章列表',pagination=pagination,category=category)

@app.route('/art/del/<int:id>')
def art_del(id):
    # 根据id删除文章
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()

    flash('删除文章成功')
    return redirect('/art/list/')

@app.route('/captcha/')
def captcha():
    c = Captcha()
    info = c.create_captcha()
    image = os.path.join(app.config['BASE_DIR'],'static/captcha/') + info['image_name']
    # 读取验证码
    with open(image,'rb') as f:
        image = f.read()
    # 获取验证码具体字母和数字
    session['captcha'] = info['captcha']
    return Response(image,mimetype='jpeg')

# @app.route('/')
# def login():
#     return 'ok'



if __name__ == '__main__':
    app.run()