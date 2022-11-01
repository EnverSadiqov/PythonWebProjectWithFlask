from flask_wtf import FlaskForm
from wtforms import StringField,FileField,PasswordField,TextAreaField,SubmitField,EmailField,BooleanField,IntegerField

class ProductForm(FlaskForm):
    name=StringField('Name')
    price=StringField('Price')
    amount=StringField('Amount')
    info=TextAreaField('Info')
    submit=SubmitField('Add Product') 