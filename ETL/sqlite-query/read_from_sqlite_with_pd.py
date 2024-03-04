import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("data/portal_mammals.sqlite")
df = pd.read_sql_query("SELECT * from surveys", con)

# Verify that result of SQL query is stored in the dataframe
print(df.head())

con.close()

#########################################################################

from sqlalchemy import create_engine
engine = create_engine("sqlite:///european_database.sqlite")
conn = engine.connect()

output = conn.execute("SELECT * FROM Student")
print(output.fetchall())