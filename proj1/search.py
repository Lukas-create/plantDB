import geopandas as gpd
import xlsx as data
from xlsx import habitat_search
from gdal import ogr
from shapely.geometry import Point
shp_driver = ogr.GetDriverByName("ESRI Shapefile")


def searchByHabitat():
    Habitat = input('Enter name of habitat\n')
    habitat_search('Habitat', Habitat)


def pointinbound(filename, x, y, Gebietsname):

    file_shape = gpd.read_file(filename)
    polygon = list(file_shape.geometry)[0]
    point = Point(x, y)
    if polygon.contains(point):
        data.habitat_search('Habitat', Gebietsname)
    else:
        print('Koordinaten außerhalb von \n' + Gebietsname + '\n')


def searchbycods():
    x = float(input('Enter x coordinate\n'))
    y = float(input('Enter y coordinate\n'))
    pointinbound(os.path.abspath("..") + "\Shape\Alpenvorland2.shp", x, y, 'Alpenvorland')
    pointinbound('D:\GitHub\Riverengineering\Shape\oberer rhein.shp', x, y, 'Oberrheingebiet')
    pointinbound('D:\GitHub\Riverengineering\Shape\Tiefland Rhein.shp', x, y, 'Niederrheinisches Tiefland')

def question():
    print('Enter 1 to seach by Habitat \n Enter 2 to search by coordinates')
    src=int(input('Enter here:'))

    if src==1:
        searchByHabitat()
    elif src ==2:
        searchbycods()
    else:
        print('no data')

question()




