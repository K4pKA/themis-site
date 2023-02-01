from flask import render_template, redirect, flash, request
from flask_login import login_user
from werkzeug.security import check_password_hash

from app import app, login_manager
from app.forms import LoginForm
from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
def index():
    return render_template('index.html', title='Themis - Главная')


@app.route('/download')
def download():
    return render_template('download.html', title='Themis - Загрузка',
                           title_page="Загрузка",
                           subtitle_page="Тут вы можете скачать программу")


@app.route('/attestation')
def attestation():
    return redirect("https://onlinetestpad.com/g36jaiblccgfe", 301)