import MySQLdb         #pip install mysqlclient
import pandas as pd

try:
    dbConnection = MySQLdb.connect(host="localhost",    # your host, usually localhost
                                   user="daniel",       # your username
                                   password ="gogogo",  # your password
                                   db="bike")          # name of the data base
    
    
    cursor = dbConnection.cursor()
    
    # Aufgabe 1 
    sqlSelectString = "SELECT Name, Gehalt FROM personal WHERE Gehalt > 3000"
    
    #Aufgabe 2
    sqlSelectString = "SELECT SUM(Anzahl) as Anzahl FROM reservierung"
    
    #Aufgabe 3
    sqlSelectString = """
                SELECT Artnr, Bezeichnung
                FROM Lager, Artikel
                WHERE ANr = ArtNr AND Bestand - Mindbest - Reserviert < 3
                """
    
    #Aufgabe 4
    sqlSelectString = """
                SELECT Artnr,
                SUM(Anzahl) as `Summe Einzelteile`
                FROM Teilestruktur
                GROUP BY Artnr
                """
    
    
    #Aufgabe 5
    sqlSelectString = """
                SELECT Reservierung.Artnr, Artikel.Bezeichnung, Reservierung.Anzahl
                
                FROM auftragsposten
                INNER JOIN Reservierung ON Auftragsposten.PosNr = Reservierung.Posnr
                INNER JOIN Artikel ON  Artikel.Anr = Reservierung.Artnr
                
                WHERE Auftragsposten.AuftrNr = 2
                """
    
    
    #Aufgabe 6
    sqlSelectString = """
    
                """
    
    
    #Aufgabe 7
    
    sqlSelectString = """
                SELECT *
                FROM Lager
                """
    
    #    sqlString = """
    #                UPDATE Lager 
    #                SET Lager.Bestand = 40
    #                WHERE Lager.Artnr = 500002
    #                """
    
    
    
    #sqlString = "SELECT * FROM personen WHERE Vorname = 'Gunter'"
    
    #    sqlString = """SELECT
    #                    PANNr,
    #                    Vorname,
    #                    Nachname,
    #                    Telefon
    #                    
    #                    FROM `personen`
    #                    
    #                    JOIN pers_telefon
    #                    ON personen.pers_telefon_ID = pers_telefon.ID
    #                    
    #                    WHERE PANNr = '4711' OR PANNr = '9999' """  
    
    
    dataFrame = pd.read_sql(sqlSelectString, dbConnection);
    
    print()
    print(dataFrame, "\n")
    
       # print(dataFrame['Artnr'][1], "\n")
    
    for index, row in dataFrame.iterrows():
        if row['Artnr'] == 500002:
            print(dataFrame['Bestand'][index])
            print(row['Artnr'], row['Bestand'])
            #row['Bestand'] += 7
            dataFrame['Bestand'][index] = 40
           # print(row['Artnr'], row['Bestand'])    
    
    print()
    print(dataFrame, "\n")
    
    
    
    
    
    #dbConnection.close()
    
    
    #dataFrame.to_sql("Lager", dbConnection)
    #dataFrame.to_sql(con=dbConnection, name='Lager', if_exists='replace', flavor='mysql')
    
    
    sqlUpdateString = """UPDATE Lager SET Lager.Bestand = 999 WHERE Artnr = 500002"""
    cursor.execute(sqlUpdateString)
    dbConnection.commit()
    
    
    
    dbConnection.close()

except:
    print("Oops, something went wrong")
    
else:
    print("Looks like everything was fine ... ")