from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):

    # productName = StringField('ProductName', validators=[DataRequired(), Length(min=2, max=20)])
    productName = StringField('ProductName')
    averageRate = SelectField(
        'AverageRate',
        choices=[('1', '>= 1'), ('2', '>= 2'), ('3', '>= 3'), ('4', '>= 4')],
        validators=[DataRequired()]
    )
    groups = SelectField(
        'Groups',
        choices=[
            ('All', 'All'),
            ('Book', 'Book'),
            ('Music', 'Music'),
            ('DVD', 'DVD'),
            ('Video', 'Video'),
            ('Toy', 'Toy'),
            ('Video Games', 'Video Games'),
            ('Software', 'Software'),
            ('CE', 'CE'),
            ('Sports', 'Sports')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Search')
