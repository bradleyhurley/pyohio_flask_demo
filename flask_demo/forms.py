from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length


class SearchForm(FlaskForm):
    search_value = StringField('search_value', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('search')
