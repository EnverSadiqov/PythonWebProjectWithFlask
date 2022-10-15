from ran import db,app


class Messages(db.Model):
    id = db.Column(db.Integer,primary_key=True,)
    name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(20),nullable=False)
    message =db.Column(db.String(200),nullable=False)
    m_data= db.Column(db.String(200))


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,)
    name = db.Column(db.String(20))
    email = db.Column(db.String(100))
    password = db.Column(db.String(20))
    is_logged_in = db.Column(db.Boolean)
    
    
    
    