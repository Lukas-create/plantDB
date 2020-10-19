"""
functions related to search for vegetation matching the users input
"""
import geopandas as gpd
import numpy as np
import pandas as pd
import os
import platform
import sqlite3
from gdal import ogr
from plant import Plant
from shapely.geometry import Point

shp_driver = ogr.GetDriverByName("ESRI Shapefile")

def search_db_via_query(query):
    '''

    Args:
        query:

    Returns:

    '''
    connection = sqlite3.connect("Pflanzendaten.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plants WHERE " + query)
    content = cursor.fetchall()
    print(content)
    print("value 1 means the plant is nativ to germany")
    connection.close()

def habitat_search(column, entry):
    """function searching for vegetation matching the users input



    Args:
        column:     column in the .csv file
        entry:    entry in the .csv file

    Returns:
        nothing
    """
    df = pd.read_csv('Pflanzendaten.csv', encoding='unicode_escape')
    if platform.system() == 'Linux':
        df = pd.read_csv('Pflanzendaten.csv')
    else:
        df = pd.read_csv('Pflanzendaten.csv', encoding='unicode_escape')
    df1 = df.dropna()
    df2 = df1.to_numpy()
    def search(column,entry,df):
        df2 = df.to_numpy()
        column=df[column]
        Name=df['NameSpez']
        for i in range(len(column)):
            if column[i]==entry:
                plant = Plant(df2[i, 0], df2[i, 1], df2[i, 2], df2[i, 3], df2[i, 4], df2[i, 5])
                plant.print_habitat()
        else:
            print('no data available')

    search(column, entry, df1)
    search(column, entry, df1)


def search_by_habitat():
    """after user input, habitat_search(..) gets called

    Returns:
        nothing
    """
    Habitat = input('Enter name of habitat\n')
    habitat_search('Habitat', Habitat)


def point_in_bound(filename, x, y, area):
    """function checks if the coordinates provided by the user are matching with a shapefile

    if the provided coordinates are out of bounds, a string will be printed in the console to let the user know, 
    if they are matching one of the shapefiles, habitat_search(..) gets called

    Args:
        filename: shapefilename
        x: x - coordinate
        y: y - coordinate
        area: name of the area

    Returns:
        text string to console
    """
    file_shape = gpd.read_file(filename)
    polygon = list(file_shape.geometry)[0]
    point = Point(x, y)
    if polygon.contains(point):
        habitat_search('Habitat', area)
    else:
        print('Koordinaten außerhalb von \n' + area + '\n')


def search_by_coordinates():
    """function that lets the user input coordinates

    after asking the user to input x and y coordinates,
    point_in_bound(..) gets called for the 3 provided shapefiles

    Returns:
        nothing
    """
    x = float(input('Enter x coordinate\n'))
    y = float(input('Enter y coordinate\n'))
    point_in_bound(os.path.abspath("..") + "\Shape\Alpenvorland2.shp", x, y, 'Alpenvorland')
    point_in_bound(os.path.abspath("..") + "\Shape\oberer rhein.shp", x, y, 'Oberrheingebiet')
    point_in_bound(os.path.abspath("..") + "\Shape\Tiefland.shp", x, y, 'Niederrheinisches Tiefland')

def question():
    """function to let the user decide if he wants to search by habitat in csv file, search by habitat in database or search by coordinates

    prints string in console to ask the user if he wants to search by putting in coordinates or the name of the habitat,
    furthermore is asking the user if he wants to search by the name of the habitat in the provided csv file or database

    Args:
        1: calls search_db_via_query(..)
        2: calls search_by_coordinates(..)
        3: calls search_by_habitat(..)

    Returns:
        text string 'no data' if the input is anything else then 1, 2 or 3
    """
    print('Enter 1 to seach by habitat in database\nEnter 2 to search by coordinates\nEnter 3 to search by habitat in csv file')
    src=int(input('Enter here:'))

    if src==1:
        habitat = input('Enter name of habitat\n')
        query = "habitat = '" + habitat + "'"
        search_db_via_query(query)
    elif src==2:
        search_by_coordinates()
    elif src==3:
        search_by_habitat()
    else:
        print('no data')

question()




