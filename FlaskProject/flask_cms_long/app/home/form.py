from flask import session
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired,EqualTo,ValidationError
from ..models import Users

class RegisterForm(FlaskForm):

    account = StringField(
        label='账号',
        description='账号',
        validators = [
            DataRequired('账号不能为空')
        ],
        render_kw={
            'class' : 'form-control',
            'placeholder' : '请输入账户'
        }
    )
    pwd = PasswordField(
        label='密码',
        description='密码',
        validators=[
            DataRequired('密码不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入密码'
        }
    )
    re_pwd = PasswordField(
        label='确认密码',
        description='确认密码',
        validators=[
            DataRequired('确认密码不能为空'),
            EqualTo('pwd', message='两次密码不一致')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入确认密码'
        }
    )
    captcha = StringField(
        label='验证码',
        description='验证码',
        validators=[
            DataRequired('验证码不能为空'),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入验证码'
        }
    )
    submit = SubmitField(
        description='注册',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

    # 自定义校验规则

    # 验证用户是否存在
    def validate_account(self,field):
        account = field.data
        user = Users.query.filter_by(account=account).count()
        if user>0:
            raise ValidationError('账户已经存在')

    # 验证验证码对不对
    def validate_captcha(self,field):
        captcha = field.data

        if not session['captcha']:
            raise ValidationError('请输入验证码')
        if session['captcha'].lower() != captcha.lower():
            raise ValidationError('验证码错误')

class LoginForm(FlaskForm):
    account = StringField(
        description='登录',
        label='登录',
        validators=[
            DataRequired('账号不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入帐户名'
        }
    )
    pwd = PasswordField(
        label='密码',
        description='密码',
        validators=[
            DataRequired('密码不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入密码'
        }
    )
    submit = SubmitField(
        description='登录',
        label='登录',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

    # 检测密码
    def validate_pwd(self,field):
        # 先检测用户是否存在
        if  not Users.query.filter_by(account=self.account.data).all():
            raise ValidationError('账户不存在')

        pwd = field.data
        user = Users.query.filter_by(account=self.account.data).first()
        if not user.check_pwd(pwd):
            raise ValidationError('密码错误')

class ArticleAddFrom(FlaskForm):
    title=StringField(
        description='文章标题',
        label='文章标题',
        validators=[
            DataRequired('文章标题不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': '输入文章标题'
        }
    )
    category = SelectField(
        description='分类',
        label='分类',
        choices = [(3,'python'),(2,'java'),(1,'php'),(4,'C')],
        default= 3,
        coerce=int,
        render_kw={
            'class':'form-control'
        }
    )
    logo = FileField(
        description='logo',
        label='logo',
        render_kw={
            'class':'form-control-file'
        }
    )
    content=TextAreaField(
        description='正文',
        label='正文',
        validators=[
            DataRequired('内容不能为空')
        ],
        render_kw={
            'style':'height:300px',
            'id':'content'# 富文本编辑器使用的id
        }
    )
    submit = SubmitField(
        description='发布文章',
        label='发布文章',
        render_kw={
            'class':'btn btn-primary'
        }
    )