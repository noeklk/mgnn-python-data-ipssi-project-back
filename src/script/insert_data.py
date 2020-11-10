import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import sqlalchemy as sa

engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')

airlines = pd.read_csv('src/static/airlines.csv')
airlines.to_sql('airlines', con=engine, if_exists='replace', index = False)

# , dtype={
#     'carrier': sa.types.VARCHAR(length=2),
#     'name': sa.types.VARCHAR(length=100)
# }

airports = pd.read_csv('src/static/airports.csv')
airports.to_sql('airports', con=engine, if_exists='replace', index = False)

# , dtype={
#     'faa': sa.types.VARCHAR(length=3),
#     'name': sa.types.VARCHAR(length=100),
#     'lat': sa.types.Float(precision=8, asdecimal=True),
#     'lon': sa.types.Float(precision=8, asdecimal=True),
#     'alt': sa.types.INTEGER(),
#     'tz': sa.types.INTEGER(),
#     'dst': sa.types.VARCHAR(length=1),
#     'tzone': sa.types.VARCHAR(length=100)
# }

flights = pd.read_csv('src/static/flights.csv')
flights.to_sql('flights', con=engine, if_exists='replace', index = False)

# , dtype={
#     'year': sa.types.VARCHAR(length=50),
#     'month': sa.types.VARCHAR(length=50),
#     'day': sa.types.VARCHAR(length=50),
#     'dep_time': sa.types.VARCHAR(length=50),
#     'sched_dep_time': sa.types.VARCHAR(length=50),
#     'dep_delay': sa.types.VARCHAR(length=50),
#     'arr_time': sa.types.VARCHAR(length=50),
#     'sched_arr_time': sa.types.VARCHAR(length=50),
#     'arr_delay': sa.types.VARCHAR(length=50),
#     'carrier': sa.types.VARCHAR(length=2),
#     'flight': sa.types.VARCHAR(length=50),
#     'tailnum': sa.types.VARCHAR(length=6),
#     'origin': sa.types.VARCHAR(length=3),
#     'dest': sa.types.VARCHAR(length=3),
#     'air_time': sa.types.VARCHAR(length=50),
#     'distance': sa.types.VARCHAR(length=50),
#     'hour': sa.types.VARCHAR(length=50),
#     'minute': sa.types.VARCHAR(length=50),
#     'time_hour': sa.types.VARCHAR(length=50)
# }

planes = pd.read_csv('src/static/planes.csv')
planes.to_sql('planes', con=engine, if_exists='replace', index = False)

weather = pd.read_csv('src/static/weather.csv')
weather.to_sql('weather', con=engine, if_exists='replace', index = False)
