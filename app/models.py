from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from . import db,login_manager
from datetime import datetime



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quiz(db.Model):

    __tablename__ = 'quizes'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    language = db.Column(db.String)
    comments = db.relationship('Comment', backref='quizes', lazy='dynamic')
    stars = db.relationship('Star', backref='quizes', lazy='dynamic')
    posted_p = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),  nullable=False)
    

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls,id):
        posts = Quiz.query.order_by(post_id=id).desc().all()
        return posts
    
    def __repr__(self):
        return f"Post {self.title}','{self.post_p}')"


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    pitched_c = db.Column(db.DateTime,default=datetime.utcnow)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizes.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch):
        comments = Comment.query.filter_by(pitchit = pitch).all()
        return comments

    @classmethod
    def delete_comment(cls,id):
        comment = Comment.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()



    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments
    def __repr__(self):
        return f'Comment{self.comment}'

class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    pass_secure = db.Column(db.String(255))
    Quizes = db.relationship('Quiz', backref='quizes', lazy='dynamic')
    comments = db.relationship('Comment', backref='comments', lazy='dynamic')
    stars = db.relationship('Star', backref='users', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class Star(db.Model):
    __tablename__ = 'stars'

    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.Integer, default=1)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_stars(self):
        db.session.add(self)
        db.session.commit()

    def add_stars(cls, id):
        star_pitch = Star(quiz_id=id)
        star_pitch.save_stars()

    @classmethod
    def get_stars(cls, id):
        star = Star.query.filter_by(quiz_id=id).all()
        return star

    @classmethod
    def get_all_stars(cls, quiz_id):
        stars = Star.query.order_by('id').all()
        return stars

    def __repr__(self):
        return f'{self.user_id}:{self.quiz_id}'
