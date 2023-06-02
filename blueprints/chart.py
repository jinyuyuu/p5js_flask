from flask import Blueprint, render_template
from exts import db
from models import User

bp = Blueprint("chart", __name__, url_prefix="/")


@bp.route('/chart')
def chart():
    items = User.query.all()
    print(items)
    return render_template('chart.html', items=items)
