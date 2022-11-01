from flask import render_template,request, redirect, url_for, flash, jsonify
from app import app_bp

@app_bp.route('/')
def app_index():
    return render_template('app/index.html')

@app_bp.route('/about')
def app_about():
    return "this is about page"