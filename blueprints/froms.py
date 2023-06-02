import wtforms
from wtforms.validators import email, Length
from models import User
from exts import db


class loginForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=5, max =5,message="用户名长度错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误！")])


def validata_username(self,filed):
    username = filed.data
    user = User.query.filter_by(username = username).first()
    if user:
        raise wtforms.ValidationError(message="该用户已经被注册！")