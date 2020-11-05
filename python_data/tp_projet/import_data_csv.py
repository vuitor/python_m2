import csv
import psycopg2
conn = psycopg2.connect("host=postgres dbname=test user=test password=test")
cur = conn.cursor()
cur.execute('DROP TABLE attrition')
conn.commit()
cur.execute("""
    CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    age text,
    attrition boolean,
    businessTravel varchar,
    dailyRate integer,
    Department varchar,
    DistanceFromHome integr,
    eduction integer,
    eductionField varchar,
    employeeCount integer,
    employeeNumber integer,
    environmentSatisfaction integer,
    gender varchar,
    hourlyRate inteher,
    jobInvolvement integer,
    jobLevel integer,
    jobRole varchar
)
""")
conn.commit()
with open('../data/attrition.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Ne pas faire le header
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (DEFAULT,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        row
    )
conn.commit()