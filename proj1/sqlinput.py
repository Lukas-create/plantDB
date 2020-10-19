import csv
import sqlite3

connection = sqlite3.connect("Pflanzendaten.db")
cursor = connection.cursor()


sql_command = """
CREATE TABLE IF NOT EXISTS plants (
species VARCHAR(255),
name VARCHAR(255),
nativ BOOLEAN,
type VARCHAR(255),
occurance VARCHAR(255),
habitat VARCHAR(255),
waterdepthmin VARCHAR(255),
waterdepthmax  VARCHAR(255),
rootdepth VARCHAR(255),
floodheightmax VARCHAR(255),
floodloss VARCHAR(255),
floodduration VARCHAR(255),
PRIMARY KEY (species, name, habitat)
);"""

cursor.execute(sql_command)

sql_command = """
INSERT INTO plants (species,name,nativ,type,occurance,habitat,waterdepthmin,waterdepthmax,rootdepth,floodheightmax,floodloss,floodduration)
VALUES (:species, :name, :nativ, :type, :occurance, :habitat, :waterdepthmin, :waterdepthmax, :rootdepth, :floodheightmax, :floodloss, :floodduration)
"""

#with open("Pflanzendaten3.csv") as csvdatei:
    #csv_reader_object = csv.reader(csvdatei, delimiter=',')

    #with sqlite3.connect("Pflanzendaten.db") as connection:
        #cursor = connection.cursor()
        #cursor.executemany(sql_command, csv_reader_object)

cursor.execute("SELECT * FROM plants")
content = cursor.fetchall()
print(content)




