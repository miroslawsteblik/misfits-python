### ETL05 - NYC data load to PostgreSQL[NYCProject] using SocrataAPI and sqlalchemy - currently through CSV
##

from sqlalchemy import create_engine
from socrata_api import df_api,df_csv
import config as config



#df = NYC_package.SocrataAPI.dfAPI()
df = df_csv()

# to obtain credentials
host = config.host
database = config.dbname
user = config.user
password = config.password

# connect to postgresl
conn_string = f'postgresql://{user}:{password}@{host}:5432/{database}'
db = create_engine(conn_string)
conn = db.connect()
# load to postgresl
df.to_sql('NYC_from_CSV', con=conn, if_exists='replace', index=False)

#close connection
conn.close()

