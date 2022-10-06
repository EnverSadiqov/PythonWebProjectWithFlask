from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
from models import *
from routes.messages import *
    
if __name__ == '__main__':
    app.run(debug=True)