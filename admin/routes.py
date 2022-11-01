from flask import render_template,request, redirect, url_for, flash, jsonify
from admin import admin_bp
from admin.forms import ProductForm

@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')

@admin_bp.route('/about')
def admin_about():
    return "this is about page"


@admin_bp.route('/create', methods =['GET','POST'])
def admin_product_create():
    productForm = ProductForm
    return render_template('admin/create.html', productForm=productForm)