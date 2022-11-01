from flask import Flask ,request, render_template, redirect,url_for,flash, jsonify


main=Flask(__name__)


#import Blueprint
from app import app_bp
from admin import admin_bp
from app.route import *
from admin.route import *

#register Blueprint

main.register_blueprint(app_bp)
main.register_blueprint(admin_bp)

@main.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    main.run(debug=True)