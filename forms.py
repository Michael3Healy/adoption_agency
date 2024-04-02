from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, AnyOf, URL, Length

class AddPetForm(FlaskForm):
    '''Form for adding a pet'''

    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], 'We only accept cats, dogs, and porcupines')])
    photo_url = StringField('Photo URL', validators=[URL(), Optional()])
    age = IntegerField('Age', validators=[NumberRange(0, 30)])
    notes = StringField('Notes')

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")