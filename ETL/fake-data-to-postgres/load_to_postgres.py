### ### Fake data load to PostgreSQL[NYCProject] using Faker and psycopg2 AND
## Retrieve Data from Tables
#
# psycopg2-tutorial/main.py
# https://earthly.dev/blog/psycopg2-postgres-python/

import psycopg2
from psycopg2 import OperationalError

# to odtain credentials
from db_config import get_db_info
filename='db_info.ini'
section='postgres-sample-db'
db_info = get_db_info(filename,section)

db_connection = None

try:
    db_connection = psycopg2.connect(**db_info)
    print("Successfully connected to the database.")

    # creating a database cursor.
    #They let you query databases and fetch results just the way file handlers let you perform I/O operations on files.

    db_cursor = db_connection.cursor()

    # create table 'people'
    create_table = '''CREATE TABLE people(
                              id SERIAL PRIMARY KEY,
                              name varchar(50) NOT NULL,
                              city varchar(40),
                              profession varchar(60));'''
    db_cursor.execute(create_table)

    # create first manual record
    insert_record = "INSERT INTO people (name,city,profession) \
    VALUES (%s, %s, %s);"
    insert_value = ('Jane Lee', 'Rustmore', 'Rust programmer')
    db_cursor.execute(insert_record, insert_value)

    # create fake records
    from fake_data import generate_fake_data

    records = tuple(generate_fake_data(100))  # cast into a tuple for immutability
    insert_record = "INSERT INTO people (name,city,profession)\
    VALUES (%s, %s, %s);"

    for record in records:
        db_cursor.execute(insert_record, record)


    ## for the changes to persist in the database, you’ll have to commit the transaction.
    db_connection.commit()

    ## Retrieve Data from Tables
    db_cursor.execute("SELECT * FROM people;")
    print(db_cursor.fetchone())

    for record in db_cursor.fetchmany(10):
        print(record)

except OperationalError:
    print("Error connecting to the database :/")

finally:
    if db_connection:
        db_connection.close()
        print("Closed connection.")
