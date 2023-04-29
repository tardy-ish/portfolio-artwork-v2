from flask import Flask, render_template, redirect
import os
import json

app = Flask(__name__)

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
def contact(lang):
    tls = json.load(open('./static/translations.json',encoding='utf-8'))
    return render_template(
        'bio.html',
        bio="active",
        lang=lang,
        content=tls[lang],
    )

@app.route('/<lang>/contact')
def bio(lang):
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
    paintings = json.load(open('./static/paintings.json',encoding='utf-8'))
    # paintings = new_images('./static/assets/artworks_new')
    return render_template(
        'artworks.html',
        art="active",
        lang=lang,
        content=tls[lang],
        src='artworks_compressed',
        paintings=paintings[lang]
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