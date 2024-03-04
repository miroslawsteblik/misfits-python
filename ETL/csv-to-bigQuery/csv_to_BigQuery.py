"""
ETL - CSV to BigQuery database.
https://www.datacourses.com/an-api-based-etl-pipeline-with-python-part-1-259/

"""
from google.cloud import bigquery
import pandas as pd
from google.oauth2 import service_account

# Read in the trades_sample_header.csv into a dataframe
# Source: http://optionsdata.baruch.cuny.edu/data1/delivery/data/trades_sample_header.csv
df = pd.read_csv("trades_sample_header.csv")
# Convert the trading_date_time to a datetime64 data type. 2012-08-21 04:12:16.827
df['trading_date_time'] = pd.to_datetime(df['trading_date_time'], format='%Y-%m-%d %H:%M:%S.%f')

project_id = 'my-project-bikes-409612'
# Full path to the new table  project.dataset.table_name
table_id = 'my-project-bikes-409612.Bikes_First_ETL.Bike1'

# Authorisation code
credential = service_account.Credentials.from_service_account_file(r"C:\Users\miros\PycharmProjects\Hello_World1\Python_ms\dataAnalyst\ETL\Credentials\my-project-bikes-409612-c44e8bf9470a.json")
client = bigquery.Client(credentials=credential, project=project_id)


# Set up a job configuration
job_config = bigquery.LoadJobConfig()
# Submit the job
job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
# Wait for the job to complete and then show the job results
job.result()
# Read back the properties of the table
table = client.get_table(table_id)
print("Table:", table.table_id, "has", table.num_rows, "rows and", len(table.schema), "columns")