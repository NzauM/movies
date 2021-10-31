from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    title = StringField('Review Title', validators = [Required()])
    review = TextAreaField('movie Review', validators = [Required()])
    submit = SubmitField('submit')

