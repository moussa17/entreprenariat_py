from flask import render_template, session, redirect, url_for 
from . import home
from .. import db


@home.route('/') 
def acceuil():
    return render_template('home/accueil.html')

