from ran import db,app
import datetime

class Messages(db.Model):
    id = db.Column(db.Integer,primary_key=True,)
    name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(20),nullable=False)
    message =db.Column(db.String(200),nullable=False)
    m_data= db.Column(db.String(200))


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,)
    name = db.Column(db.String(20),nullable=False)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(30),nullable=False)
    info = db.Column(db.String(255),nullable=False)
    
    
    