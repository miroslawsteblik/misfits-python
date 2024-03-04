#### https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples ####

### Import sqlite file with sqlalchemy and pandas ###

import sqlalchemy as db
import pandas as pd

db_name = "chinook.db"
engine = db.create_engine(f'sqlite:///{db_name}')

#check table names
insp = db.inspect(engine)
print(insp.get_table_names())

# query
query1 = "SELECT * FROM albums"
query3 = "SELECT Title, Name FROM albums INNER JOIN artists on albums.ArtistId = artists.ArtistId"
query2 = "SELECT * FROM artists"
query4 = "SELECT * FROM playlist_track INNER JOIN tracks ON playlist_track.TrackId = Tracks.TrackId WHERE Milliseconds < 250000"

## using sqlalchemy
con = engine.connect()
res = con.execute(db.text(query1))
df = pd.DataFrame(res.fetchall())
con.close()

## using Pandas
df2 = pd.read_sql_query(query2, engine)
df3 = pd.read_sql_query(query3, engine)
df4 = pd.read_sql_query(query4, engine)

print(df.head())
print(df2.head())
print(df3.head())
print(df4.head())
