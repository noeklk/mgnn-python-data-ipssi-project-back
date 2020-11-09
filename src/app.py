import secrets

from flask import Flask, redirect, render_template, request, session, url_for

SECRET_KEY = secrets.token_urlsafe(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def view_index():
    return render_template('index.html')
