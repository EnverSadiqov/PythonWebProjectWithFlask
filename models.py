from start import db
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Integer)
    amount=db.Column(db.Integer)
    info=db.Column(db.Text)