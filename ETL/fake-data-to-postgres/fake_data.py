# psycopg2-tutorial/fake_data.py
from faker import Faker

fake = Faker()
Faker.seed(42) #Without the seed, you’ll get a different set of records every time you run the script.

def generate_fake_data(num):
    records = []

    for i in range(num):
        name, city, job = fake.name(), fake.city(), fake.job()
        records.append((name,city,job))
    return records