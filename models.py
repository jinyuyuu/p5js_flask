
from datetime import datetime
from exts import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(400))
    age = db.Column(db.Integer())

    def __repr__(self):
        return f'<User {self.username}>'






#join_time = db.Column(db.DateTime, default = datetime.now)