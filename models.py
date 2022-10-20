from start import db

#generate class with prodcutName and prodcutPrice
class Product(db.Model):
    id=db.Column(db.Integer,primery_key=True ,autoincrement= True)
    prodcutName=db.Column(db.String(100),nullable=True )
    prodcutPrice=db.Column(db.Integer,nullable=True )
    is_active=db.Column(db.Boolean,default=True)
    add_date=db.Column(db.DataTime)
    