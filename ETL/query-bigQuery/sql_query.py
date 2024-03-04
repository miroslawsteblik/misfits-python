
from google.cloud import bigquery
from google.oauth2 import service_account

# Authorisation code
credential = service_account.Credentials.from_service_account_file(r"C:\Users\miros\PycharmProjects\Hello_World1\Python_ms\dataAnalyst\ETL\Credentials\my-project-bikes-409612-c44e8bf9470a.json")
client = bigquery.Client(credentials=credential)

### SQL query

sql_query = 'SELECT MAX(value) AS max_unemployment_rate FROM `bigquery-public-data.bls.unemployment_cps`  WHERE series_title="(Unadj) Unemployment Rate" '
# Schedule a job to run the query
query_job = client.query(sql_query)
# Fetch the results of the query
query_results = query_job.result()
# Loop through the results and print out one of the columns
for row in query_results:
    print(row)


### Obtaining BigQuery Dataset Metadata

dataset_name = 'bigquery-public-data.bls'
# Access the INFORMATION_SCHEMA for the dataset
dataset = client.get_dataset(dataset_name)
# Give a description of the data set
print("Description: ", dataset.description)


## Show a list of the tables contained in the dataset

# First get a list of the tables
tables = client.list_tables(dataset)
# For each table in the list, get the table details
for table in tables:
    table_detail = client.get_table(str(table.full_table_id).replace(':','.'))
    print("Table: ", table.table_id, " has ", table_detail.num_rows, " rows.")

## To get the schema details for a specific table, provide the complete path

full_table_path = 'bigquery-public-data.bls.unemployment_cps'
# Access the table details
table_detail = client.get_table(full_table_path)
# Print out the full schema information
print("Table schema: ", table_detail.schema)
# Show just the column names and data types
for schemafield in table_detail.schema:
   print(schemafield.name, schemafield.field_type, schemafield.mode)