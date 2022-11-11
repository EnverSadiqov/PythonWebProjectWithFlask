from flask import render_template,request, redirect, url_for, flash, jsonify
from admin import admin_bp
from admin.forms import ProductForm

@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')



@admin_bp.route('/products',methods=['GET','POST'] )
def admin_products():
    from start import db
    from models import Product
    products=Product.query.all()
    productform=ProductForm()
    if request.method=='POST':
        name=productForm.name.data
        price=productForm.price.data
        amount=productForm.amount.data
        info=productForm.info.data
        product=Product(name=name,price=price,amount=amount,info=info)
        db.session.add(product)
        db.session.commit() 
        return redirect ('/admin/products')
    return render_template('admin/products.html', productform=productsform,products=products) 

