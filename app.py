from flask import Flask, render_template, redirect, request, flash
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




@app.route('/')
@app.route('/<lang>')
def landing(lang='en'):
    print(app.config['MAIL_DEFAULT_SENDER'])
    return render_template(
        'landing.html',
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
        if form_data == {}:
            form_data = dict(request.args)
        # print(args_data)
        client_message = clientMessage(
            recepient=form_data['email'],
            name=form_data['name'],
            message=form_data['message']
        )

        # mail.connect()
        mail.send(client_message)
        # status = ['d-none','']

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
    return render_template(
        'artworks.html',
        art="active",
        lang=lang,
        content=tls[lang],
        src='images/artworks_prepped',
        paintings=paintings
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