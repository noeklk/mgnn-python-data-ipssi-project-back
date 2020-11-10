import secrets
import json
from flask import Flask, redirect, render_template, request, session, url_for, jsonify
import pandas as pd
from sqlalchemy import create_engine 
import configparser

# config = configparser.ConfigParser()

# print(config)

#airlines = pd.read_csv('src/static/airlines.csv')

#airlines.to_sql('airlines', con=engine, if_exists='replace', index = False)

engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')



SECRET_KEY = secrets.token_urlsafe(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def view_index():
    with engine.connect() as con:
        #df = con.execute("SELECT * FROM weather")
        print(pd.read_sql_table("flights", con))

    
    return render_template('index.html')

@app.route('/api/1-airport-airline-destination-plane-timezone-count')
def return_res():
    res = engine.execute("SELECT * FROM airlines").fetchall()
    
    return json.dumps(res)
