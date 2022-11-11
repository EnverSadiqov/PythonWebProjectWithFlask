from flask import Flask ,request, render_template, redirect,url_for,flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

main=Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
main.config['SECRET_KEY'] ="secretkey"
db=SQLAlchemy(main)
migrate=Migrate(main,db)


from models import *
from app.routes import *
from admin.routes import *

#import Blueprint
from app import app_bp
from admin import admin_bp

#register Blueprint
main.register_blueprint(app_bp)
main.register_blueprint(admin_bp)

@main.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    main.run(debug=True)