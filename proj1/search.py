"""
function functionality related to searching for matching Vegetation in Pflanzendaten.csv
"""
import geopandas as gpd
import numpy as np
import pandas as pd
import os
import platform
from gdal import ogr
from plant import Plant
from shapely.geometry import Point

shp_driver = ogr.GetDriverByName("ESRI Shapefile")

def habitat_search(Spalte, eintrag):
    """
    Args:
        Spalte:     Spalte in der .csv Datei
        eintrag:    Zeile in der .csv Datei

    Returns:
        Nichts
    """
    df = pd.read_csv('Pflanzendaten.csv', encoding='unicode_escape')
    if platform.system() == 'Linux':
        df = pd.read_csv('Pflanzendaten.csv')
    else:
        df = pd.read_csv('Pflanzendaten.csv', encoding='unicode_escape')
    df1 = df.dropna()
    df2 = df1.to_numpy()
    def search(Spalte,eintrag,df):
        df2 = df.to_numpy()
        Spalte=df[Spalte]
        Name=df['NameSpez']
        for i in range(len(Spalte)):
            if Spalte[i]==eintrag:
                plant = Plant(df2[i, 0], df2[i, 1], df2[i, 2], df2[i, 3], df2[i, 4], df2[i, 5])
                plant.print_habitat()
        else:
            print(' ')

    search(Spalte, eintrag, df1)


def search_by_habitat():
    """Nach eingabe des Gebietsnamens wird habitat_search aufgerufen

    Returns:
        Nichts
    """
    Habitat = input('Enter name of habitat\n')
    habitat_search('Habitat', Habitat)


def point_in_bound(filename, x, y, Gebietsname):
    """hilfsfunktion checkt ob die eingegebenen Koordinaten in einer der vorhandenen Shapefiles liegen.

    wenn Koordinaten außerhalb liegen wird es als Text ausgegeben, wenn sie innerhalb einer der
    Shapefiles liegen wird die habitat_search Funktion aufgerufen

    Args:
        filename: Name der Shapefile
        x: X - Koordinate
        y: Y - Koordinate
        Gebietsname: Name der Shapefile, entsprechend dem Gebietsnamen

    Returns:
        Nichts
    """
    file_shape = gpd.read_file(filename)
    polygon = list(file_shape.geometry)[0]
    point = Point(x, y)
    if polygon.contains(point):
        habitat_search('Habitat', Gebietsname)
    else:
        print('Koordinaten außerhalb von \n' + Gebietsname + '\n')


def search_by_coordinates():
    """ermöglicht es Koordinaten in der Konsole einzugeben

    Nachdem die Koordinaten von dem Benutzer in der Konsole eingegeben wurden, wird die Funktion point_in_bound aufgerufen
    für jede der drei bisher vorhandenen Shapefiles

    Returns:
        Nichts
    """
    x = float(input('Enter x coordinate\n'))
    y = float(input('Enter y coordinate\n'))
    point_in_bound(os.path.abspath("..") + "\Shape\Alpenvorland2.shp", x, y, 'Alpenvorland')
    point_in_bound(os.path.abspath("..") + "\Shape\oberer rhein.shp", x, y, 'Oberrheingebiet')
    point_in_bound(os.path.abspath("..") + "\Shape\Tiefland.shp", x, y, 'Niederrheinisches Tiefland')

def question():
    """Funktion ruft je nach Eingabe des benutzers search_by_habitat oder search_by_coordinates aus

    Frägt in der Konsole nach, ob der Benutzer nach dem gewünschten Habitat oder Koordinaten suchen will
    und ruft dem entsprechend search_by_habitat oder seach_by_coordinates auf

    Args:
        1: Suche nach Habitat
        2: Suche nach Koordinaten

    Returns:
        Nichts
    """
    print('Enter 1 to seach by Habitat \n Enter 2 to search by coordinates')
    src=int(input('Enter here:'))

    if src==1:
        search_by_habitat()
    elif src==2:
        search_by_coordinates()
    else:
        print('no data')

question()




