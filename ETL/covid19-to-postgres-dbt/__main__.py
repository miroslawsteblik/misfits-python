### ETL05 - covid-19 data load to PostgreSQL[covid-19]

from sqlalchemy import create_engine
from sqlalchemy.types import Integer, DateTime, String, Float
import config as config
import pandas as pd


# to obtain credentials
host = config.host
database = config.dbname
user = config.user
password = config.password

# connect to postgresl
conn_string = f'postgresql://{user}:{password}@{host}:5432/{database}'
db = create_engine(conn_string)
conn = db.connect()


DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"
df = pd.read_csv(DATA_URL)


### load to postgresl - table1
DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"
df = pd.read_csv(DATA_URL)
df.to_sql(
    "covid_latest",  # table name
    con=conn,
    if_exists='replace',
    index=False,  # In order to avoid writing DataFrame index as a column
    dtype={
        "last_updated_date": DateTime(),
        "total_cases": Integer(),
        "new_cases": Integer()
    }
)


df = pd.read_sql_table(
    "covid19",  # table name
    con=conn,
)

