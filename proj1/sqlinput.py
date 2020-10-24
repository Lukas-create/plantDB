import csv
import sqlite3
from tabulate import tabulate

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
waterdepthmin INTEGER(255),
waterdepthmax  INTEGER(255),
rootdepth INTEGER(255),
floodheightmax INTEGER(255),
floodloss REAL(255),
floodduration INTEGER(255),
PRIMARY KEY (species, name, habitat)
);"""

cursor.execute(sql_command)


def inputquestion():
    src = int(input('Enter here:'))
    if src == 1:

        with open(input('enter csv-filename')+'.csv') as csvdatei:
            csv_reader_object = csv.reader(csvdatei, delimiter=',')

            with sqlite3.connect("Pflanzendaten.db") as connection:
                cursor = connection.cursor()
                sql_command = """
                INSERT INTO plants (species,name,nativ,type,occurance,habitat,waterdepthmin,waterdepthmax,rootdepth,floodheightmax,floodloss,floodduration)
                VALUES (:species, :name, :nativ, :type, :occurance, :habitat, :waterdepthmin, :waterdepthmax, :rootdepth, :floodheightmax, :floodloss, :floodduration)
                """
                cursor.executemany(sql_command, csv_reader_object)
    elif src == 2:
        connection = sqlite3.connect("Pflanzendaten.db")
        cursor = connection.cursor()
        sql_command = (input('''Insert sql command'''))
        cursor.execute(sql_command)
        cursor.execute("COMMIT")
    else:
        print('only able to import data to table using csv file or sql command')


inputquestion()
cursor.execute("SELECT * FROM plants")
content = cursor.fetchall()
print(tabulate((content), headers=['species','name','nativ','type','occurance','habitat','waterdepthmin','waterdepthmax','rootdepth','floodheightmax','floodloss','floodduration']))



