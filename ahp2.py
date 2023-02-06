#Importing Libraries
import arcpy
import arcpy
import numpy as np
import numpy
from array import array
import math
import os
#Getting the table path and creating another table with a suffix CI
TablepathC=arcpy.GetParameterAsText(0)
arcpy.management.Copy(str(TablepathC),str(TablepathC)+"CI")
Tablepath=str(TablepathC)+"CI"
#Converting the table to array
arr = arcpy.da.TableToNumPyArray(Tablepath,"*")
#doing all the math
Cursor=arcpy.da.SearchCursor(Tablepath,"*")
l=0

for row in Cursor:
    l=l+1
    j = list(row[2:30])
    if l==1:
        u=np.array(j)
    else:
        u = numpy.vstack([u, j]) 
del Cursor

d=u.sum(axis=0)
Matsize=math.sqrt(u.size)
#Error Trap1
if Matsize<2:
    arcpy.AddError("Habboub: SORRY, The Min. number of raster layers is 2. You cannot continue")
g=u*(1/d)
k=(1/Matsize)*(g.sum(axis=1))
ws=numpy.dot(u,k.T)
hh=ws*(1/k)
lamda=hh.mean()
Matsize=math.sqrt(u.size)
#Error Trap2
if Matsize<2:
    arcpy.AddError("Habboub: SORRY, The Min. number of raster layers is 2. You cannot continue")
ci=(lamda-Matsize)/(Matsize-1)
#adding all necessary  fields
arcpy.management.AddField(Tablepath,"weight","DOUBLE")
arcpy.management.AddField(Tablepath,"CI","DOUBLE")
arcpy.management.AddField(Tablepath,"RI","DOUBLE")
arcpy.management.AddField(Tablepath,"CR","DOUBLE")
arcpy.management.AddField(Tablepath,"Notes","TEXT")

#filling the new columns
# filling the "weight" column
cursor2 = arcpy.da.UpdateCursor(Tablepath, ["weight"])
n=0
for row2 in cursor2:
    cursor2.updateRow([k[n]])
    n=n+1
del cursor2
# filling the "CI" column
cursor3 = arcpy.da.UpdateCursor(Tablepath, ["CI"])
n=0
for row3 in cursor3:
    cursor3.updateRow([ci])
    n=n+1
del cursor3
# filling the "RI" column
cursor4 = arcpy.da.UpdateCursor(Tablepath, ["RI"])
n=0
RItable = {'1.0': 0, '2.0': 0, '3.0': 0.58,'4.0': .9, '5.0': 1.12, '6.0': 1.24,'7.0': 1.36, '8.0': 1.41, '9.0':1.45 ,'10.0': 1.49, '11.0': 1.51, '12.0':1.54 ,'13.0':1.56, '14.0':1.57 , '15.0': 1.58}
CISRTING=str(Matsize)
for row4 in cursor4:
    cursor4.updateRow([RItable[CISRTING]])
    n=n+1
del cursor4
CR=ci/RItable[CISRTING]
# filling the "CR" column
cursor5 = arcpy.da.UpdateCursor(Tablepath, ["CR"])
n=0
for row5 in cursor5:
    cursor5.updateRow([CR])
    n=n+1
del cursor5
# filling the "Notes" column
cursor6 = arcpy.da.UpdateCursor(Tablepath, ["Notes"])
n=0
for row6 in cursor6:
    if CR<=1:
        cursor6.updateRow(["The matrix is considered to be consistent enough."])
    else:
        cursor6.updateRow(["The comparison matrix should be improved."])
    n=n+1
del cursor6
#Done
