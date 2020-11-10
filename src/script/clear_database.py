from sqlalchemy import create_engine
from sqlalchemy.sql import text

truncate_query_1 = text("""TRUNCATE TABLE airlines""")
truncate_query_2 = text("""TRUNCATE TABLE flights""")
truncate_query_3 = text("""TRUNCATE TABLE planes""")
truncate_query_4 = text("""TRUNCATE TABLE airports""")
truncate_query_5 = text("""TRUNCATE TABLE weather""")

engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')

with engine.connect() as con:
    con.execute(truncate_query_1)
    con.execute(truncate_query_2)
    con.execute(truncate_query_3)
    con.execute(truncate_query_4)
    con.execute(truncate_query_5)