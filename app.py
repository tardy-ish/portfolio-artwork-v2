from flask import Flask, render_template, redirect, request
import os
import json

import config

from flask_mail import Mail,Message


app = Flask(__name__)
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
    if request.method == 'POST':
        form_data = dict(request.form)
        msg = Message(
            subject='Hey',
            # sender='spidey.ds@hotmail.com',
            recipients=['daksh301200@gmail.com']
        )
        msg.body = 'This is a test email'
        mail.send(msg)
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    return render_template(
        'contact.html',
        contact="active",
        lang=lang,
        content=tls[lang],
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