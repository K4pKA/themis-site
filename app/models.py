from app import db
from flask_login import UserMixin

ROLE_USER = 0
ROLE_MODER = 1
ROLE_ADMIN = 2
ROLE_SUPER_ADMIN = 3


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    login = db.Column(db.String(64), unique=True, nullable=False)
    nickname = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True, nullable=True)
    surname = db.Column(db.String(64), index=True, nullable=True)
    custom_postname = db.Column(db.String(32), index=True, nullable=True)
    birth_date = db.Column(db.DateTime(), nullable=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(32), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER, nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.id)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(350))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    likes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    last_edition_timestamp = db.Column(db.DateTime)
    last_edition_user_ud = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Article %r>' % (self.title)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    last_edition_timestamp = db.Column(db.DateTime)
    last_edition_user_ud = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Comment %r>' % (self.id)


class AnswerComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    likes = db.Column(db.Integer)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    last_edition_timestamp = db.Column(db.DateTime)
    last_edition_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Answer %r>' % (self.id)


class License(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    HWID = db.Column(db.String)
    date_end = db.Column(db.DateTime)
    key = db.Column(db.String)

    def __repr__(self):
        return '<License %r>' % (self.hwid)