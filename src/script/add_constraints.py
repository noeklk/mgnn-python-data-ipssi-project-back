from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('mysql+pymysql://root@localhost:8081/airport-analytics?charset=utf8mb4')

add_fk_flights = text("""ALTER TABLE flights ADD FOREIGN KEY (tailnum) REFERENCES planes(tailnum)""")
add_fk_planes = text("""ALTER TABLE planes ADD FOREIGN KEY (carrier) REFERENCES airlines(carrier)""")
add_fk_weather = text("""ALTER TABLE weather ADD FOREIGN KEY (faa) REFERENCES airports(faa)""")

add_constraint_airport_airline_airline = text("""ALTER TABLE airline_airport ADD CONSTRAINT `constr_airline_airport_airline_fk` ADD FOREIGN KEY (airline_carrier) REFERENCES airlines(carrier) ON DELETE CASCADE ON UPDATE CASCADE""")
add_constraint_airport_airline_airport = text("""ALTER TABLE airline_airport ADD CONSTRAINT `constr_airline_airport_airport_fk` ADD FOREIGN KEY (airport_faa) REFERENCES airports(faa) ON DELETE CASCADE ON UPDATE CASCADE""")


with engine.connect() as con:
    con.execute(add_fk_flights)
    # con.execute(add_fk_planes)
    # con.execute(add_fk_weather)
    # con.execute(add_constraint_airport_airline_airline)
    # con.execute(add_constraint_airport_airline_airport)