#Importing Libraries
import arcpy
import numpy as np
import numpy
from array import array
import math
import os
#pointing to the current opened mxd
mxd = arcpy.mp.ArcGISProject("CURRENT")
#Pointing to top dataframe in the mxd (REGARDLESS OF IT ACTIVITNESS)
df = mxd.listMaps("Map")[0]
#listing all the layers in that dataframe
listlyr= df.listLayers()

#Getting the name of the geodatabase and the table 
geodatabase=arcpy.GetParameterAsText(0)
Tablename=arcpy.GetParameterAsText(1)
Tablepath= fr"{geodatabase}\\{Tablename}"

#Creating a new table
arcpy.management.CreateTable(geodatabase, Tablename)

#Adding the first column
arcpy.management.AddField(Tablepath,"layername","TEXT")

#listing only raster layer in that first columns
n=0
for lyr in listlyr:
    if lyr.isRasterLayer == True:
        arcpy.management.AddField(Tablepath,lyr.name,"DOUBLE")
        n=n+1

cursor = arcpy.da.InsertCursor(Tablepath, ["layername"])
#if there is no raster layers in that columns, an error will appear 
if n==0:
        cursor.insertRow(["Habboub: No Raster Data, SORRY, you cannot continue"])
        arcpy.AddError("Habboub: No Raster Data, SORRY, you cannot continue")
else:
    for lyr in listlyr:
        if lyr.isRasterLayer == True:
            cursor.insertRow([lyr.name])
            n=n+1
del cursor
