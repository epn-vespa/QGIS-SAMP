## with VOTable t
## generate Shapefile, preserving geometry, geographic coordinate system

import shapefile
import numpy as np

w = shapefile.Writer(shapefile.POLYGON)
for colname in t.colnames: w.field(colname)

def getParts(sRegion):
    lon=sRegion.split(' ')[2:][0::2]
    llon=np.asarray([float(i) for i in lon])
    spread=llon.max()-llon.min() ###
    if spread > 180:
        lon = [[x, x-360][x>180] for x in llon]
    lat=sRegion.split(' ')[2:][1::2]
    return [[[360-float(lon[i]),float(lat[i])] for i in range(len(lat))]]

def writeRecord(rowNumber):
    w.poly(getParts(t['s_region'][rowNumber]))
    w.record(*list(t[rowNumber].as_void()))

for i in range(len(t)): writeRecord(i)
w.save('test')
