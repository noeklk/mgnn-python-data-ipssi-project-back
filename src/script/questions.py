from sqlalchemy import create_engine
from flask import jsonify
engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')

def json_to_dict(json_response, query):
    return jsonify({'result': [dict(row) for row in json_response], 'query': query})

def question1():
    f = open("mysql/init/init.sql", "r")
    question_1_sql = """"""
    with f as file:
        question_1_sql = f"""{file.read()}"""
        

    return jsonify({'result': question_1_sql})

def question2():
    question_2_query = """SELECT (
        SELECT COUNT(*)
        FROM   airlines
        ) AS airlines_count,
        (
        	SELECT COUNT(*)
        	FROM   airports
        ) AS airports_count,
        (
            SELECT COUNT(DISTINCT dest)
            FROM flights
        ) AS flights_distinct_dest_count,
         (
            SELECT COUNT(*)
            FROM planes
        ) AS planes_count,
        (
            SELECT COUNT(DISTINCT tzone)
            FROM airports
        ) AS airports_distinct_tzone_count
        FROM DUAL;"""

    with engine.connect() as con:
        result_2 = con.execute(question_2_query).fetchall()

        return json_to_dict(result_2, question_2_query)

def question3():
    question_3_query = """SELECT COUNT(DISTINCT tzone) AS tzone_count FROM airports WHERE dst = 'N' AND tzone LIKE '%%America%%';"""
    with engine.connect() as con:
        result = con.execute(question_3_query).fetchall()

        return json_to_dict(result, question_3_query)

def question4():
    question_4_1_query = """select origin AS airport_origin_faa, count(*) AS flights_count, air_p.name AS airport_name
    from flights
    JOIN airports air_p ON air_p.faa = flights.origin
    group by origin
    order by COUNT(origin) DESC
    LIMIT 1"""

    question_4_2_1_query = """select dest AS airport_destination_faa, count(*) AS flights_count, air_p.name AS airport_name, air_p.tzone AS destination_tzone
    from flights
    JOIN airports air_p ON air_p.faa = flights.dest
    group by dest
    order by COUNT(dest) DESC
    LIMIT 10"""

    question_4_2_2_query = """select dest AS airport_destination_faa, count(*) AS flights_count, air_p.name AS airport_name, air_p.tzone AS destination_tzone
    from flights
    JOIN airports air_p ON air_p.faa = flights.dest
    group by dest
    order by COUNT(dest) ASC
    LIMIT 10"""

    question_4_3_1_query = """select f.tailnum, count(*) AS flights_count, p.model AS plane_model, p.manufacturer AS plane_manufacturer
    from flights AS f
    JOIN planes p ON p.tailnum = f.tailnum
    group by f.tailnum
    order by COUNT(f.tailnum) DESC
    LIMIT 10"""

    question_4_3_2_query = """select f.tailnum, count(*) AS flights_count, p.model AS plane_model, p.manufacturer AS plane_manufacturer
    from flights AS f
    JOIN planes p ON p.tailnum = f.tailnum
    group by f.tailnum
    order by COUNT(f.tailnum) ASC
    LIMIT 10"""

    with engine.connect() as con:
        result_4_1 = con.execute(question_4_1_query).fetchall()

        result_4_2_1 = con.execute(question_4_2_1_query).fetchall()
        result_4_2_2 = con.execute(question_4_2_2_query).fetchall()

        result_4_3_1 = con.execute(question_4_3_1_query).fetchall()
        result_4_3_2 = con.execute(question_4_3_2_query).fetchall()

        json = jsonify(
            {
                'result_4_1': [dict(row) for row in result_4_1], 
                'query_4_1': question_4_1_query,

                'result_4_2_1_most': [dict(row) for row in result_4_2_1],
                'query_4_2_1_most': question_4_2_1_query,

                'result_4_2_2_least': [dict(row) for row in result_4_2_2],
                'query_4_2_2_least': question_4_2_2_query,

                'result_4_3_1_most': [dict(row) for row in result_4_3_1],
                'query_4_3_1_most': question_4_3_1_query,

                'result_4_3_2_least': [dict(row) for row in result_4_3_2],
                'query_4_3_2_least': question_4_3_2_query,
            })

        return json

def question5():
    question_5_1_query = """select airlines.name AS airline_name, f.carrier AS airline_carrier_code, count(DISTINCT(f.dest)) AS dest_count
    from flights AS f
    JOIN airlines ON airlines.carrier = f.carrier
    group by airlines.carrier
    order by dest_count DESC"""

    question_5_2_query = """select airlines.name AS airline_name, f.carrier AS airline_carrier_code, airports.name AS origin_airport_name, f.origin, count(distinct f.dest) as dest_count
    from flights AS f
    JOIN airlines ON airlines.carrier = f.carrier
    JOIN airports ON airports.faa = f.origin
    group by airlines.carrier, f.origin
    order by dest_count desc"""


    with engine.connect() as con:
        result_5_1 = con.execute(question_5_1_query).fetchall()
        result_5_2 = con.execute(question_5_2_query).fetchall()

        json = jsonify(
            {
                'result_5_1': [dict(row) for row in result_5_1], 
                'query_5_2': question_5_1_query,

                'result_5_2': [dict(row) for row in result_5_2], 
                'query_5_2': question_5_2_query,
            })

        return json

def question6():
    question_6_1_query = """SELECT count(*) AS flights_count
    FROM flights
    WHERE flights.dest IN ('IAH', 'HOU');"""

    question_6_2_1_query = """SELECT COUNT(*) AS flights_count 
    FROM flights 
    JOIN airports airports_nyc ON airports_nyc.tzone = 'America/New_York' 
    WHERE flights.origin = airports_nyc.faa AND flights.dest = 'SEA';"""

    question_6_2_2_query = """SELECT COUNT(DISTINCT airlines.name) AS airlines_count
    FROM airlines
    JOIN flights ON flights.dest = 'SEA'
    WHERE airlines.carrier = flights.carrier;"""

    question_6_2_3_query = """SELECT COUNT(DISTINCT flights.tailnum) AS tailnum_count FROM flights WHERE flights.dest = 'SEA'"""


    with engine.connect() as con:
        result_6_1 = con.execute(question_6_1_query).fetchall()
        result_6_2_1 = con.execute(question_6_2_1_query).fetchall()
        result_6_2_2 = con.execute(question_6_2_2_query).fetchall()
        result_6_2_3 = con.execute(question_6_2_3_query).fetchall()

        json = jsonify(
            {
                'result_6_1': [dict(row) for row in result_6_1], 
                'query_6_1': question_6_1_query,

                'result_6_2_1': [dict(row) for row in result_6_2_1], 
                'query_6_2_1': question_6_2_1_query,

                'result_6_2_2': [dict(row) for row in result_6_2_2], 
                'query_6_2_2': question_6_2_2_query,

                'result_6_2_3': [dict(row) for row in result_6_2_3], 
                'query_6_2_3': question_6_2_3_query,
            })

        return json