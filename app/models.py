from app import db

ROLE_USER = 0
ROLE_MODER = 1
ROLE_ADMIN = 2
ROLE_SUPER_ADMIN = 3


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64))
    password = db.Column(db.String(32))
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(350))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
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


class License(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    hwid = db.Column(db.String)
    date_end = db.Column(db.DateTime)
    key = db.Column(db.String)

    def __repr__(self):
        return '<License %r>' % (self.hwid)