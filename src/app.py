import secrets
import json
from flask import Flask, redirect, render_template, request, session, url_for, jsonify
import pandas as pd
from sqlalchemy import create_engine 
from src.script.questions import question2, question3, question4, question5, question6, question1
from src.script.custom_data import origin_to_dest_data, airline_carrier_total_delay_in_hours, airport_total_delay_in_hours
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
        n = i+1
        print(n)
        url_array.append([f"return_question{n}", n])

    return url_array

@app.route('/')
def view_index():   
    return render_template('index.html', routes = get_routes())

@app.route('/api/question-1', methods=['GET'])
def return_question1():
    return question1()

@app.route('/api/question-2', methods=['GET'])
def return_question2():
    return question2()

@app.route('/api/question-3', methods=['GET'])
def return_question3():
    return question3()

@app.route('/api/question-4' , methods=['GET'])
def return_question4():
    return question4()

@app.route('/api/question-5' , methods=['GET'])
def return_question5():
    return question5()


@app.route('/api/question-6' , methods=['GET'])
def return_question6():
    return question6()

@app.route('/api/origin_to_dest_gps_data', methods=['GET'])
def get_origin_to_dest_gps_data():
    return origin_to_dest_data()


@app.route('/api/airline_carrier_total_delay_in_hours', methods=['GET'])
def get_airline_carrier_total_delay_in_hours():
    return airline_carrier_total_delay_in_hours()

@app.route('/api/airport_total_delay_in_hours', methods=['GET'])
def get_airport_total_delay_in_hours():
    return airport_total_delay_in_hours()
