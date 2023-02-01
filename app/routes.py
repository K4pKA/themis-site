from flask import render_template, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Themis - Главная')


@app.route('/download')
def download():
    return render_template('download.html', title='Themis - Загрузка',
                           title_page="Загрузка",
                           subtitle_page="Тут вы можете скачать программу")


@app.route('/attestation')
def attestation():
    return redirect("https://onlinetestpad.com/g36jaiblccgfe", 301)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Themis - Авторизация',
                           title_page="Авторизация",
                           subtitle_page="Страница авторизации пользователей", form=form)