import geopandas as gpd
import xlsx as data
from gdal import ogr
from shapely.geometry import Point
shp_driver = ogr.GetDriverByName("ESRI Shapefile")
shp_dataset1 = shp_driver.Open("D:\GitHub\Riverengineering\Shape\Alpenvorland2.shp")
shp_dataset2 = shp_driver.Open('D:\GitHub\Riverengineering\Shape\oberer rhein.shp')
shp_dataset3 = shp_driver.Open('D:\GitHub\Riverengineering\Shape\RHEIN1.shp')
def pointinbound(file, a, b, Gebietsname):
    shp_layer = file.GetLayer()
    shp_srs = shp_layer.GetSpatialRef()
    file_shape = gpd.read_file(file)
    polygon = list(file_shape.geometry)[0]
    point = Point(a, b)
    if polygon.contains(point):
        data.habitat_search('Habitat', Gebietsname)
    else:
        print('Koordinaten außerhalb der Gebiete')

pointinbound(shp_dataset1, 1295243, 6161799, 'Alpenvorland')
pointinbound(shp_dataset2, 1295243, 6161799, 'Oberrheingebiet')
pointinbound(shp_dataset3, 1295243, 6161799, 'Unterrheingebiet')


