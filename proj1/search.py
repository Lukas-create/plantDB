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
from tabulate import tabulate
import gdal
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
    print(tabulate((content), headers=['species','name','nativ','type','occurance','habitat','waterdepthmin','waterdepthmax','rootdepth','floodheightmax','floodloss','floodduration']))
    print("\nvalue 1 means the plant is nativ to germany")
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
    def search(column,entry,df):
        df2 = df1.to_numpy()
        column = df[column]
        for i in range(len(column)):
            if column[i] == entry:
                plant = Plant(df2[i, 0], df2[i, 1], df2[i, 2], df2[i, 3], df2[i, 4], df2[i, 5], df2[i, 6], df2[i, 7], df2[i, 8], df2[i, 9], df2[i, 10], df2[i, 11])
                plant.print_habitat()
        else:
            print('no data')

    search(column, entry, df1)

def search_by_habitat():
    """after user input, habitat_search(..) gets called

    Returns:
        nothing
    """
    habitat = input('Enter name of habitat\n')
    habitat_search('habitat', habitat)

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
        habitat_search('habitat', area)
        print('Enter 1 if you want elevation data for the coordinates\nEnter 2 if you dont want elevation data')
        src = int(input('Enter here:'))

        if src == 1:
            elevation(x, y)
        elif src == 2:
            print('done')
    else:
        print('\ncoordinates out of \n' + area + '\nplease check provided shapefile for suitable coordinates\n')

def search_by_coordinates():
    """function that lets the user input coordinates

    after asking the user to input x and y coordinates,point_in_bound(..) gets called for the 3 provided shapefiles,
    afterwards the user gets asked if he wants to receive elevation data for the input coordinates

    Returns:
        nothing
    """
    x = float(input('Enter x coordinate\n'))
    y = float(input('Enter y coordinate\n'))
    point_in_bound(os.path.abspath("..") + "\Shape\Alpenvorlandgesamt.shp", x, y, 'Alpenvorland')
    point_in_bound(os.path.abspath("..") + "\Shape\oberrheinmaintiefland.shp", x, y, 'Oberrheingebiet')
    point_in_bound(os.path.abspath("..") + "\Shape\Tiefland.shp", x, y, 'Niederrheinisches Tiefland')

def elevation(x, y):
    file = os.path.abspath("..") + "\Shape\Shape.vrt"
    layer = gdal.Open(file)
    gt = layer.GetGeoTransform()
    rasterx = int((x - gt[0]) / gt[1])
    rastery = int((y - gt[3]) / gt[5])
    print('elevation =', layer.GetRasterBand(1).ReadAsArray(rasterx,rastery, 1, 1)[0][0], 'm above sea level')

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
    print('Enter 1 to search by habitat in database with detailed information\nEnter 2 to search by coordinates\nEnter 3 to search by habitat in csv file for a quick overview without detail')
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




