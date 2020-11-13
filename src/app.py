import secrets
import json
from flask import Flask, redirect, render_template, request, session, url_for, jsonify
import pandas as pd
from sqlalchemy import create_engine 
from src.script.questions import question2, question3, question4, question5, question6
from flask_cors import CORS

SECRET_KEY = secrets.token_urlsafe(16)

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = SECRET_KEY

engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')

questions_count = 5

def get_routes():
    url_array = []
    for i in range(questions_count):
        n = i+2
        print(n)
        url_array.append([f"return_question{n}", n])

    return url_array

@app.route('/')
def view_index():   
    return render_template('index.html', routes = get_routes())

@app.route('/api/question-2')
def return_question2():
    return question2()

@app.route('/api/question-3')
def return_question3():
    return question3()

@app.route('/api/question-4')
def return_question4():
    return question4()

@app.route('/api/question-5')
def return_question5():
    return question5()


@app.route('/api/question-6')
def return_question6():
    return question6()