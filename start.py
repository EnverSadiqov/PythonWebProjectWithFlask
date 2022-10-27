from flask import Flask,render_template,request ,redirect, url_for ,flash ,jsonify
main = Flask(__name__)
from app.routes import *
from admin.routes import *

#import Blueprint
from app import app_bp
from admin import admin_bp
#register the blueprint
main.register_blueprint(app_bp)
main.register_blueprint(admin_bp)


@main.route('/')
def index():
    return render_template('index.html')
    

if __name__ == '__main__':
    main.run(debug=True)    