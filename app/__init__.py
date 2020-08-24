from flask import Flask, render_template 
from flask_bootstrap import Bootstrap 
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy 
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__) 
    app.config.from_object(config[config_name]) 
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    from app.home import home as home_blueprint
    from app.admin import admin as admin_blueprint 
    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint)

    return app




'''from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '493c67c24a70073460784d4e682e103e'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entreprenariat.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entreprenariat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

'''