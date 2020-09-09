# we assume that 'layer' is a polygon layer
from numpy import record
from osgeo import ogr

source = ogr.Open("D:\GitHub\Riverengineering\Shape\Alpenvorland2.shp")
layer = source.GetLayer()
schema = []
ldefn = layer.GetLayerDefn()
for n in range(ldefn.GetFieldCount()):
    fdefn = ldefn.GetFieldDefn(n)
    schema.append(fdefn.name)
print
['dip_dir', 'dip', 'cosa', 'sina']


