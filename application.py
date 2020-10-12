import os
from flask import Flask
from flask import render_template, flash, redirect
from forms import CardGeneratorForm

from deckart import generate
from config import Config

application = Flask(__name__)
application.config.from_object(Config)

@application.route("/", methods=['GET', 'POST'])
def index():
    form = CardGeneratorForm()
    img = None
    if form.validate_on_submit():
        key, error = generate(card_name=form.card_name.data, title=form.title.data)
        if key:
            img = f"https://d1tv6m53xyhfh2.cloudfront.net/{key}"
            return render_template('index.html', form=form, img=img)
        else:
            return render_template('index.html', form=form, img=None, error=error)
    return render_template('index.html', form=form)

if __name__ == "__main__":
    application.run(port=5000, debug=True)