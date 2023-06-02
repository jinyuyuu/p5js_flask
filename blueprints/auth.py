from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from wtforms import form
from exts import db

from models import User
from .froms import loginForm

bp = Blueprint("auth", __name__, url_prefix="/auth")


# /index/login就是一个前缀



@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        age = request.form.get('age')
        print("username", username)
        user = User(username=username, password=generate_password_hash(password), age=age)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.result"))


@bp.route('/result', methods=['GET', 'POST'])
def result():  # put application's code here
    people = User.query.all()
    print(people)
    return render_template('result.html', people=people)



