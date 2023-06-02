from flask import Flask, render_template
import config
from exts import db
from gevent import pywsgi
from models import User

from flask_migrate import Migrate

from blueprints.auth import bp as auth_bp

from blueprints.chart import bp as chart_bp

# from blueprints.result import bp as result_bp



app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

# 不是一开始就绑定，
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(chart_bp)



@app.route('/')
def helloworld():
    return 'hello world!'



if __name__ == '__main__':
    app.run()



