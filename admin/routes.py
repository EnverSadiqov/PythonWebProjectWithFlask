from flask import render_template,request, redirect, url_for, flash, jsonify
from admin import admin_bp
from admin.forms import ProductForm

@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')

