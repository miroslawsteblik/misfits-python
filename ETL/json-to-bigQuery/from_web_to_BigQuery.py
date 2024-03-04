
### ETL02 - JSON (hosted on website) to BigQuery database.
# https://www.datacourses.com/an-api-based-etl-pipeline-with-python-part-1-259/


"""currently there is an error with loading into BigQuery some of the column names"""

import requests
import pandas as pd
from datetime import datetime
from google.cloud import bigquery
from google.oauth2 import service_account


### Extracting

url = 'https://gbfs.lyft.com/gbfs/2.3/bkn/en/station_information.json'
r = requests.get(url)

### Transforming

stations = r.json()['data']['stations']
last_updated = r.json()['last_updated']
dt_object = datetime.fromtimestamp(last_updated).strftime('%Y-%m-%d %H:%M:%S')
print(dt_object)

df = pd.json_normalize(stations)
df['date'] = dt_object

### Load

## To CSV
df.to_csv("citibike_stations_data.csv")

## To BigQuery
project_id = 'my-project-bikes-409612'
table_id = 'my-project-bikes-409612.Bikes_First_ETL.Bike1'

# Authorisation code
credential = service_account.Credentials.from_service_account_file(r"my-project-bikes-409612-c44e8bf9470a.json")
client = bigquery.Client(credentials=credential, project=project_id)

# Load the data
job_config0 = bigquery.LoadJobConfig(write_disposition = 'WRITE_TRUNCATE')
job = client.load_table_from_dataframe(df, table_id, job_config=job_config0)
job.result()

""" currently there is an error with loading into BigQuery some of the column names"""