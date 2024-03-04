""" Getting Started with NYC OpenData and the Socrata API
https://holowczak.com/getting-started-with-nyc-opendata-and-the-socrata-api/5/ """

import pandas as pd
from sodapy import Socrata

data_url='data.cityofnewyork.us'    # The Host Name for the API endpoint (the https:// part will be added automatically)
data_set='erm2-nwe9'    # The data set at the API endpoint (311 data in this case)
app_token='kzbDKb3dgcFUJVANZwPDHU6mt'   # The app token created in the prior steps
client = Socrata(data_url,app_token)      # Create the client to point to the API endpoint
# Set the timeout to 100 seconds
client.timeout = 100
# Retrieve the first 2000 results returned as JSON object from the API
# The SoDaPy library converts this JSON object to a Python list of dictionaries
results = client.get(data_set, limit=100)

#results = client.get(data_set, where="complaint_type = 'Unsanitary Animal Pvt Property' ", limit=2000) #filters
data = r"C:\Users\miros\PycharmProjects\Hello_World1\my_py_scripts\Data Engineer\ETL\socrata-to-postgres\data\my_311_data.csv"

# create dfAPI
def df_api():
    df = pd.DataFrame.from_records(results)
    return df

def df_csv():
    df = pd.DataFrame.from_records(results)
    df.to_csv(data)
    df_read= pd.read_csv(data)
    return  df_read

# api = dfAPI()
# print(api['location'])
#
# result = requests.get(api_url, headers=headers, params=params)
# next_50_cafes = json_normalize(result.json()["businesses"])






