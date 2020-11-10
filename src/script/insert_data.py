import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')

airlines = pd.read_csv('src/static/airlines.csv')
airlines.to_sql('airlines', con=engine, if_exists='replace', index = False)

airports = pd.read_csv('src/static/airports.csv')
airports.to_sql('airports', con=engine, if_exists='replace', index = False)

flights = pd.read_csv('src/static/flights.csv')
flights.to_sql('flights', con=engine, if_exists='replace', index = False)

planes = pd.read_csv('src/static/planes.csv')
planes.to_sql('planes', con=engine, if_exists='replace', index = False)

weather = pd.read_csv('src/static/weather.csv')
weather.to_sql('weather', con=engine, if_exists='replace', index = False)
