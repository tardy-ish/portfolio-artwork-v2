from flask import Flask, render_template, redirect, request, flash
import json

import config

from flask_mail import Mail
from mailing import clientMessage

from datetime import datetime

import logging

#Logging setup
logger = logging.getLogger()
consoleHandler = logging.StreamHandler()
logger.addHandler(consoleHandler)

file_name = datetime.now().strftime("%Y-%m-%d-%H-%M")

fileHandler = logging.FileHandler(f"./logs/{file_name}.log")
logger.addHandler(fileHandler)

app = Flask(__name__)
app.secret_key = 'wot be this'
app.config.from_object(config.DevelopmentConfig)
mail = Mail(app)





@app.route('/')
def base_en():
    return redirect('/en')

@app.route('/<lang>')
def base_ar(lang):
    return render_template(
        'base.html',
        lang=lang
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

@app.route('/<lang>/contact',methods=['GET','POST'])
def contact(lang):
    status = ['','d-none']
    if request.method == 'POST':
        form_data = dict(request.form)
        client_message = clientMessage(
            recepient=form_data['email'],
            name=form_data['name'],
            message=form_data['message']
        )
        mail.send(client_message)
        status = ['d-none','']

        # mail.send(msg)
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    return render_template(
        'contact.html',
        contact="active",
        lang=lang,
        content=tls[lang],
        status=status,
    )

@app.route('/<lang>/contactp')
def contactp(lang):
    
    pass

@app.route('/<lang>/selected_works')
def artworks(lang):
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    paintings = json.load(open('./static/assets/paintings.json',encoding='utf-8'))
    return render_template(
        'artworks.html',
        art="active",
        lang=lang,
        content=tls[lang],
        src='images/artworks_prepped',
        paintings=paintings
    )

@app.route('/index')
def index():
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    lang = 'en'
    return render_template(
        'index.html',
        lang=lang,
        content=tls[lang]
    )


if __name__ == '__main__':

    app.run(debug=True)