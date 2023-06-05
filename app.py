from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import json

import config

from flask_mail import Mail
from mailing import clientMessage

from datetime import datetime

import logging
import os

#Logging setup
logger = logging.getLogger()
consoleHandler = logging.StreamHandler()
logger.addHandler(consoleHandler)

file_name = datetime.now().strftime("%Y-%m-%d-%H-%M")

fileHandler = logging.FileHandler(f"./logs/{file_name}.log")
logger.addHandler(fileHandler)

app = Flask(__name__)
app.config.from_object(config.ProductionConfig)
if os.getenv('env') == 'dev':
    app.config.from_object(config.DevelopmentConfig)
app.secret_key = 'wot be this'

mail = Mail(app)
db = SQLAlchemy(app)


class artwork(db.Model):
    order = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(80), primary_key=True)
    size = db.Column(db.String(20))
    details = db.Column(db.String(40))
    year = db.Column(db.String(10))
    file = db.Column(db.String(40), unique=True)
    pass



@app.route('/')
@app.route('/<lang>')
def landing(lang='en'):
    return redirect(f'/{lang}/home')


@app.route('/<lang>/home')
def home(lang='en'):
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    return render_template(
        'home.html',
        home="active",
        lang=lang,
        content=tls[lang],
    )



@app.route('/<lang>/bio')
def bio(lang):
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    return render_template(
        'bio.html',
        bio="active",
        lang=lang,
        content=tls[lang],
    )

@app.route('/<lang>/contact')
def contact(lang):
    status = ['','d-none']
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    return render_template(
        'contact.html',
        contact="active",
        lang=lang,
        content=tls[lang],
        status=status,
    )


@app.route('/<lang>/selected_works')
def artworks(lang):
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    paintings = json.load(open('./static/assets/paintings.json',encoding='utf-8'))
    # paintings = artwork.query.order_by(artwork.order).all()
    # paintings = [painting.__dict__ for painting in paintings]
    # paintings = os.listdir('./static/assets/images/gallery_prepped')
    # paintings = [painting for painting in paintings if painting.endswith('.jpg')]
    print(paintings)
    return render_template(
        'artworks2.html',
        art="active",
        lang=lang,
        content=tls[lang],
        src='images/gallery_prepped',
        paintings=paintings
    )

@app.route('/<lang>/exhibitions')
def exhibitions(lang):
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    return render_template(
        'exhibitions.html',
        exhibitions="active",
        lang=lang,
        content=tls[lang]
    )

@app.route('/<lang>/publications')
def publications(lang):
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    return render_template(
        'publications.html',
        publications="active",
        lang=lang,
        content=tls[lang]
    )


if __name__ == '__main__':

    app.run(debug=True)