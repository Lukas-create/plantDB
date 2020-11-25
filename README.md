# Python tool to search for suitable vegetation regarding NBS

To run this tool properly make sure to import and install all the used libraries in search.py and sqlinput.py. To make sure that the provided shapefiles and the Shape.vrt file with the used elevation data can be used, they must be saved in the same directory as the python script and kept in the 'Shape' directory. Renaming any of the provided files will also result in the tool not properly working.  To use the provided csv file it is also demanded for it to be saved in the project directory. The python version used to create the tool was Python 3.7. To use your own data table without any issues you need to make sure that it inherits the same amount of arguments as the provided plantdata.csv file or make sure to change the amount of columns used in the habitat_search function and the amount of argmuents in the created class 'Plant' accordingly.


