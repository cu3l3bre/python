import MySQLdb
import pandas as pd

try:
    dbConnection = MySQLdb.connect(host="localhost",    # your host, usually localhost
                                   user="daniel",       # your username
                                   password ="gogogo",  # your password
                                   db="mydb")           # name of the data base
    
    #sqlString = "SELECT * FROM personen"
    #sqlString = "SELECT * FROM personen WHERE Vorname = 'Gunter'"
    
    sqlString = """SELECT
                    PANNr,
                    Vorname
                    ,Nachname,
                    Telefon
                    
                    FROM `personen`
                    
                    JOIN pers_telefon
                    ON personen.pers_telefon_ID = pers_telefon.ID
                    
                    WHERE PANNr = '4711' OR PANNr = '9999' """  
    
    
    dataFrame = pd.read_sql(sqlString, dbConnection);
    
    print()
    print(dataFrame, "\n")
    #print(dataFrame['Vorname'][1], "\n")
    
    dbConnection.close()
    
except:
    print("Oops, something went wrong")
    
else:
    print("Looks like everything was fine ... ")