from flask import session
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired,EqualTo,ValidationError
from models import User

# 注册表单
class RegisterForm(FlaskForm):
    account = StringField(
        description='账号',
        validators=[
            DataRequired('账号不能为空')
        ],
        render_kw={
            'class' : 'form-control',
            'placeholder' : '请输入账户'
        }
    )
    pwd = PasswordField(
        description='密码',
        validators=[
            DataRequired('密码不能为空')
        ],
        render_kw={
            'class' : 'form-control',
            'placeholder' : '请输入密码'
        }
    )
    re_pwd = PasswordField(
        description='确认密码',
        validators=[
            DataRequired('确认密码不能为空'),
            EqualTo('pwd',message='两次密码不一致')
        ],
        render_kw={
            'class' : 'form-control',
            'placeholder' : '请输入确认密码'
        }
    )
    captcha = StringField(
        description='验证码',
        validators=[
            DataRequired('验证码不能为空'),
        ],
        render_kw={
            'class' : 'form-control',
            'placeholder' : '请输入验证码'
        }
    )
    submit = SubmitField(
        description='注册',
        render_kw={
            'class' : 'btn btn-primary'
        }
    )

    # 验证用户是否存在
    def validate_account(self,field):
        account = field.data
        user = User.query.filter_by(account=account).count()
        if user > 0: # 用户已经存在
            # 抛出异常
            raise ValidationError('账户已经存在')

    # 验证码校验
    def validate_captcha(self,field):
        # 获取用户输入的验证码
        captcha = field.data

        if not session['captcha']:
            raise ValidationError('非法操作')
        if session['captcha'].lower() != captcha.lower():
            raise ValidationError('验证码错误')

# 登录表单
class LoginForm(FlaskForm):
    account = StringField(
        description='登录',
        label='登录',
        validators=[
            DataRequired('账户名不能为空')
        ],
        render_kw={
            'class' : 'form-control',
            'placeholder' : '请输入帐户名'
        }
    )
    pwd = PasswordField(
        label='密码',
        description='密码',
        validators=[
            DataRequired('密码不能为空')
        ],
        render_kw={
            'class' : 'form-control',
            'placeholder' : '请输入密码'
        }
    )
    submit = SubmitField(
        description='登录',
        label='登录',
        render_kw={
            'class' : 'btn btn-primary'
        }
    )

    def validate_pwd(self,field):
        # 获取用户提交的密码
        pwd = field.data
        # 根据用户名查询用户
        user = User.query.filter_by(account=self.account.data).first()
        if not user.check_pwd(pwd):
            raise ValidationError('密码错误')

# 文章表单
class ArticleAddForm(FlaskForm):
    title = StringField(
        description='文章标题',
        label='文章标题',
        validators=[
            DataRequired('文章标题不能为空')
        ],
        render_kw={
            'class' : 'form-control',
            'placeholder' : '输入文章标题'
        }
    )
    category = SelectField(
        description='分类',
        label='分类',
        choices=[(1,'python'),(2,'洗头'),(3,'洗澡'),(4,'洗脚')],
        default=4,
        coerce=int,
        render_kw={
            'class':'form-control'
        }
    )
    logo = FileField(
        description='logo',
        label='logo',
        render_kw={
            'class' : 'form-control-file'
        }
    )
    content = TextAreaField(
        description='文章内容',
        label='文章内容',
        validators=[
            DataRequired('内容不能为空')
        ],
        render_kw={
            'style' : 'height:300px',
            'id' : 'content' # 给富文本编辑器使用的id
        }
    )
    submit = SubmitField(
        description='发布文章',
        label='发布文章',
        render_kw={
            'class' : 'btn btn-primary'
        }
    )

# 文章编辑表单

class ArticleEditForm(ArticleAddForm):
    submit = SubmitField(
        description='保存文章',
        label='保存文章',
        render_kw={
            'class' : 'btn btn-primary'
        }
    )