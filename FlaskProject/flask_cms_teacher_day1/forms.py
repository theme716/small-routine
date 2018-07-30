from flask import session
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired,EqualTo,ValidationError
from models import User

#登陆表单

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


