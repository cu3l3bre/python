
import pandas as pd
import sqlalchemy as sql

connect_string = 'mysql://daniel:gogogo@localhost/bike'

sqlEngine = sql.create_engine(connect_string)
dbConnection = sqlEngine.connect()

sqlSelect = "SELECT * FROM Reservierung"


df = pd.read_sql_query(sqlSelect, sqlEngine)
print(df, '\n')

for index, row in df.iterrows():
    if row['Posnr'] == 101:
        df['Anzahl'][index] += 1


df.to_sql('mydatatable_temp', dbConnection, if_exists='replace', index=False);
dbConnection.execute('REPLACE INTO Reservierung (SELECT * FROM mydatatable_temp);')

df = pd.read_sql_query(sqlSelect, sqlEngine)
print(df, '\n')



dbConnection.close()