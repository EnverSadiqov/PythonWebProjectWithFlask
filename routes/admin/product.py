from start import app,db,migrate,request,redirect,url_for,flask,render_template
from models import Product
from start import 

@admin_bp.route('/product/',methods=['GET','POST'])
def product():
    from model import db,Product
    products = Products()
    data = Product.query.all()
    if request.method =='POST':
        productName = products.productName.data
        productM=Product(productName=productName,productPrice=productPrice,)
        db.session.add(productM)
        db.session.commit()
        return redirect('/admin/product')
    return render_template('admin/product.html',products=products,data=data)

# Product update hissəsi

@admin_bp.route('/product/edit/<id>',methods=['GET','POST'])
def edit(id):
    product = Products()
    from models import Product,db
    data = Product.query.get(id)
    if request.method=='POST':
        data.productName=product.productName.data
        data.productPrice=product.productPrice.data
        db.session.commit()
        return redirect('/admin/product')
    return render_template('admin/update.html',product=product,data=data)

# Product delete hissəsinin

@admin_bp.route('/product/delete/<id>')
def delete(id):
    from model import Product,db
    data = Product.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/admin/product')