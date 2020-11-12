from sqlalchemy.sql import text
import sqlalchemy as sa
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')

# ------------------------- AIRPORTS -------------------------
airports = pd.read_csv('src/static/airports.csv')

airports.fillna(np.nan, inplace = True)
airports = airports[airports['faa'].str.match(pat = "^[A-Z0-9]{3}$", na=False) == True]

airports.to_sql('airports', con=engine, if_exists='append', index = False)
# ------------------------- WEATHER -------------------------
weather = pd.read_csv('src/static/weather.csv')

weather.fillna(np.nan, inplace = True)
weather.replace(r'\s+', np.nan, regex=True, inplace=True)
weather['time_hour'] = pd.to_datetime(weather['time_hour'], errors='coerce').values.astype('datetime64[us]')
weather = weather[weather.origin.isin(airports['faa'])]

weather.to_sql('weather', con=engine, if_exists='append', index = False)

# ------------------------- AIRLINES -------------------------
airlines = pd.read_csv('src/static/airlines.csv')

airlines.fillna(np.nan, inplace = True)

airlines.to_sql('airlines', con=engine, if_exists='append', index = False)

# ------------------------- PLANES -------------------------
planes = pd.read_csv('src/static/planes.csv')

planes.fillna(np.nan, inplace = True)
planes['speed'].replace(r'\s+', np.nan, regex=True, inplace=True)
planes['year'].replace(r'\s+', np.nan, regex=True, inplace=True)

planes.to_sql('planes', con=engine, if_exists='append', index = False)

# ------------------------- FLIGHTS -------------------------
flights = pd.read_csv('src/static/flights.csv')

flights['time_hour'] = pd.to_datetime(flights['time_hour'], errors='coerce').values.astype('datetime64[us]')
flights['arr_delay'].replace(r'\s+', np.nan, regex=True, inplace=True)
flights['air_time'].replace(r'\s+', np.nan, regex=True, inplace=True)
flights['arr_time'].replace(r'\s+', np.nan, regex=True, inplace=True)
flights['dep_time'].replace(r'\s+', np.nan, regex=True, inplace=True)
flights['dep_delay'].replace(r'\s+', np.nan, regex=True, inplace=True)

flights = flights[
    (flights.dest.isin(airports['faa'])) & 
    (flights.tailnum.isin(planes['tailnum'])) &
    (flights.carrier.isin(airlines['carrier'])) &
    (flights.origin.isin(airports['faa'])) &
    (flights.year.isin(weather['year'])) &
    (flights.month.isin(weather['month'])) &
    (flights.day.isin(weather['day'])) &
    (flights.hour.isin(weather['hour'])) &
    (flights.origin.isin(weather['origin']))
    ]

flights.to_sql('flights', con=engine, if_exists='append', index = False)
