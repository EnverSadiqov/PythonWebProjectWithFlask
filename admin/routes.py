from flask import render_template, request, redirect, url_for, flash, jsonify
from admin import admin_bp

@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')

@admin_bp.route('/about')
def admin_about():
    return 'This is about page'