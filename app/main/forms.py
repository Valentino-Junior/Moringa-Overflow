from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class QuizForm(FlaskForm):
    title = StringField('Title')
    question = TextAreaField('Ask the question', validators=[DataRequired()])
    language = SelectField('Select language', choices=[('html', 'HTML'),('css', 'CSS'),('bootstrap', 'BOOTSTRAP'),('javascript', 'JAVASCRIPT'),('jquery', 'JQUERY'),('angular', 'ANGULAR'),('python-flask', 'PYTHON-FLASK'),('python-django', 'PYTHON-DJANGO'),('java-spark', 'JAVA-SPARK'),('android', 'ANDROID'),('c', 'C'),('c++', 'C++'),('others', 'OTHERS')])
    submit = SubmitField('Post')

class AnswerForm(FlaskForm):
    answer = TextAreaField('Give answer', validators=[DataRequired()])
    submit = SubmitField('Submit')