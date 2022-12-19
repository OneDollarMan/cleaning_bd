from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Optional

rus_input_required = InputRequired(message='Заполните поле')


class LoginForm(FlaskForm):
    login = StringField('login')
    password = StringField('password')
    otp = StringField('OTP (опционально)', [Optional()])
    remember_me = BooleanField('remember_me', default=False)


class RegForm(FlaskForm):
    username = StringField('username')
    fio = StringField('fio')
    password = StringField('password')


class FaForm(FlaskForm):
    otp = StringField('Введите OTP из приложения Google', [rus_input_required])
    submit = SubmitField('Включить')