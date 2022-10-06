from ran import db,app
 
class Messages(db.Model):
    id = db.Column(db.Integer,primary_key=True,)
    name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(20),nullable=False)
    message =db.Column(db.String(200),nullable=False)
