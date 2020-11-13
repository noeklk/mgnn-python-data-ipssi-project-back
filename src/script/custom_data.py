from sqlalchemy import create_engine
from flask import jsonify
import simplejson as json

engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')

def json_to_dict(json_response, query):
    return jsonify({'result': [dict(row) for row in json_response], 'query': query})

def origin_to_dest_data():
    origin_to_dest_query = """SELECT 
    DISTINCT f.origin, 
    airport_origin.name AS origin_airport_name, 
    airport_origin.lat AS origin_airport_lat, 
    airport_origin.lon AS origin_airport_lon, 
    f.dest,
    airport_dest.name AS dest_airport_name,
    airport_dest.lat AS dest_airport_lat, 
    airport_dest.lon AS dest_airport_lon
    FROM flights as f
    JOIN airports airport_origin ON airport_origin.faa = f.origin
    JOIN airports airport_dest ON airport_dest.faa = f.dest
    ORDER BY f.origin DESC;"""

    with engine.connect() as con:
        result = con.execute(origin_to_dest_query).fetchall()

        return jsonify({'result': [dict(row) for row in result]})

def airline_carrier_total_delay_in_hours():
    airline_carrier_total_delay_in_hours_query = """SELECT airlines.name AS carrier_name, FLOOR(SUM(f.dep_delay + f.arr_delay)/60) AS total_delay
    FROM flights AS f
    JOIN airlines ON airlines.carrier = f.carrier
    group by f.carrier 
    ORDER BY total_delay DESC
    LIMIT 10"""

    with engine.connect() as con:
        result = con.execute(airline_carrier_total_delay_in_hours_query).fetchall()

        return json.dumps({'result': [dict(row) for row in result]}, use_decimal=True)

def airport_total_delay_in_hours():
    airport_total_delay_in_hours_query = """SELECT DISTINCT f.origin, airports.name AS airport_name, FLOOR(SUM(f.dep_delay + f.arr_delay)/60) AS total_delay
    FROM flights AS f
    JOIN airports ON airports.faa = f.origin
    GROUP by f.origin
    ORDER BY total_delay DESC"""

    with engine.connect() as con:
        result = con.execute(airport_total_delay_in_hours_query).fetchall()

        return json.dumps({'result': [dict(row) for row in result]}, use_decimal=True)

