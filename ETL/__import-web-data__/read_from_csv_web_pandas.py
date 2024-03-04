
from urllib.request import urlretrieve
import json
import pandas as pd

# Assign url of file: url
url1 = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url1, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df1 = pd.read_csv('winequality-red.csv', sep=';')

############## Using Pandas ##################################
# Assign url of file: url
url2= 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
df2 = pd.read_csv(url2, sep=';')

# Print the head of the DataFrame
print(df1.head())
print(df2.head())