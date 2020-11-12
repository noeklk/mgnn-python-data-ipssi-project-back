from sqlalchemy import create_engine
from flask import jsonify
engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')

def json_to_dict(json_response, query):
    return jsonify({'result': [dict(row) for row in json_response], 'query': query})

def question2():
    question2_query = """SELECT (
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
        result = con.execute(question2_query).fetchall()
        return json_to_dict(result, question2_query)

def question3():
    question3_query = """SELECT COUNT(DISTINCT tzone) FROM airports WHERE dst = 'N' AND tzone LIKE '%%America%%';"""
    with engine.connect() as con:
        result = con.execute(question3_query).fetchall()
        return json_to_dict(result, question3_query)

def question4():
    question4_1_query = """select * from
    (select origin, count(origin), air_p.name AS airport_name
    from flights
    JOIN airports air_p WHERE air_p.faa = flights.origin
    group by origin
    order by origin ASC) derived_table
    LIMIT 1"""

    with engine.connect() as con:
        most_popular_airport_origin = con.execute(question4_1_query).fetchall()

        json = jsonify(
            {
                'result_most_popular_airport_origin': [dict(row) for row in most_popular_airport_origin], 
                'query_most_popular_airport_origin': question4_1_query
            })

        return json
