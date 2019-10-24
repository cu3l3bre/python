
import pandas as pd
import sqlalchemy as sql

connect_string = 'mysql://daniel:gogogo@localhost/bike'

sqlEngine = sql.create_engine(connect_string)
dbConnection = sqlEngine.connect()

sqlSelect = "SELECT * FROM Reservierung"

# Get Data from DB
df = pd.read_sql_query(sqlSelect, sqlEngine)
print(df, '\n')

# Look for PosNr 101 and add 1 to it
for index, row in df.iterrows():
    if row['Posnr'] == 101:
        df['Anzahl'][index] += 1

# Write dataframe to a new table for spamming
df.to_sql('mydatatable_temp', dbConnection, if_exists='replace', index=False);

# Replace the data in Rervierung with the data of the new table
dbConnection.execute('REPLACE INTO Reservierung (SELECT * FROM mydatatable_temp);')

# Get data again to see if it was successful
df = pd.read_sql_query(sqlSelect, sqlEngine)
print(df, '\n')

dbConnection.close()