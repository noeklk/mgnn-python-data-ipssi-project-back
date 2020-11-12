from sqlalchemy import create_engine
from flask import jsonify
engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')

def json_to_dict(json_response, query):
    return jsonify({'result': [dict(row) for row in json_response], 'query': query})

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
    question_3_query = """SELECT COUNT(DISTINCT tzone) FROM airports WHERE dst = 'N' AND tzone LIKE '%%America%%';"""
    with engine.connect() as con:
        result = con.execute(question_3_query).fetchall()

        return json_to_dict(result, question_3_query)

def question4():
    question_4_1_query = """select * from
    (select origin AS airport_origin_faa, count(*) AS flights_count, air_p.name AS airport_name
    from flights
    JOIN airports air_p WHERE air_p.faa = flights.origin
    group by origin
    order by COUNT(origin) DESC) derived_table
    LIMIT 1"""

    question_4_2_1_query = """select * from
    (select dest AS airport_destination_faa, count(*) AS flights_count, air_p.name AS airport_name, air_p.tzone AS destination_tzone
    from flights
    JOIN airports air_p WHERE air_p.faa = flights.dest
    group by dest
    order by COUNT(dest) DESC) derived_table
    LIMIT 10"""

    question_4_2_2_query = """select * from
    (select dest AS airport_destination_faa, count(*) AS flights_count, air_p.name AS airport_name, air_p.tzone AS destination_tzone
    from flights
    JOIN airports air_p WHERE air_p.faa = flights.dest
    group by dest
    order by COUNT(dest) ASC) derived_table
    LIMIT 10"""

    with engine.connect() as con:
        result_4_1 = con.execute(question_4_1_query).fetchall()
        result_4_2_1 = con.execute(question_4_2_1_query).fetchall()
        result_4_2_2 = con.execute(question_4_2_2_query).fetchall()

        json = jsonify(
            {
                'result_4_1': [dict(row) for row in result_4_1], 
                'query_4_1': question_4_1_query,

                'result_4_2_1_most': [dict(row) for row in result_4_2_1],
                'query_4_2_1_most': question_4_2_1_query,

                'result_4_2_2_least': [dict(row) for row in result_4_2_2],
                'query_4_2_2_least': question_4_2_2_query,
            })

        return json
