from flask import render_template,flash,redirect,Response,session
from models import db,app,User
from forms import RegisterForm
from werkzeug.security import generate_password_hash
from captcha import Captcha
import os

@app.route('/login/')
def login():
    return render_template('login.html',title='登陆')

@app.route('/logout/')
def logout():
    return '退出'

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

@app.route('/art/add/')
def art_add():
    return render_template('art_add.html',title='添加文章')

@app.route('/art/edit/<int:id>/')
def art_edit(id):
    return render_template('art_edit.html')

@app.route('/art/list/')
def art_list():
    return render_template('art_list.html',title='文章列表')

@app.route('/art/del/<int:id>')
def art_del(id):
    return '删除文章'

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


if __name__ == '__main__':
    app.run()