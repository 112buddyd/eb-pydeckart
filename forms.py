from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CardGeneratorForm(FlaskForm):
    card_name = StringField('Card Name', validators=[DataRequired()])
    colors = StringField('Color Override')
    # title max length is 21
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Generate')