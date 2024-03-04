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
results = client.get(data_set, limit=2000)

#results = client.get(data_set, where="complaint_type = 'Unsanitary Animal Pvt Property' ", limit=2000) #filters

# Convert the list of dictionaries to a Pandas data frame
df = pd.DataFrame.from_records(results)

# Save the data frame to a CSV file
df.to_csv("my_311_data.csv")






metadata = client.get_metadata(data_set)
[x['name'] for x in metadata['columns']]
['Unique Key', 'Created Date', 'Closed Date', 'Agency', 'Agency Name', 'Complaint Type', 'Descriptor',
'Location Type', 'Incident Zip', 'Incident Address', 'Street Name', 'Cross Street 1', 'Cross Street 2',
'Intersection Street 1', 'Intersection Street 2', 'Address Type', 'City', 'Landmark', 'Facility Type',
'Status', 'Due Date', 'Resolution Description', 'Resolution Action Updated Date', 'Community Board', 'BBL',
'Borough', 'X Coordinate (State Plane)', 'Y Coordinate (State Plane)', 'Open Data Channel Type',
'Park Facility Name', 'Park Borough', 'Vehicle Type', 'Taxi Company Borough', 'Taxi Pick Up Location',
'Bridge Highway Name', 'Bridge Highway Direction', 'Road Ramp', 'Bridge Highway Segment', 'Latitude',
'Longitude', 'Location', 'Zip Codes', 'Community Districts', 'Borough Boundaries', 'City Council Districts',
'Police Precincts']




