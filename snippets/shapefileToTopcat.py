'''
This script will load a shapefile 'shp.*' from the current directory,
it will convert it to the votable and save it as shp.xml,
it will then connect to HUB, broadcast shp.xml to listening VO 
(e.g. TOPCAT), then disconnect. 
Only records will be sent, geometry will be discarded.
'''
import shapefile
sf = shapefile.Reader("shp")
shapes = sf.shapes()
fields = sf.fields()
records = sf.records()
import numpy as np
from astropy.table import Table
fieldnames=[i[0] for i in fields]
t=Table(np.asarray(records), names=fieldnames[1:])
t.write("shp.xml", format='votable')
### broadcast it to HUB
from astropy.vo.samp import SAMPIntegratedClient
client = SAMPIntegratedClient()
client.connect()
params = {}
params["url"] = ''# local file - need to save first, eh?
params["name"] = "shp" ## table name
import urlparse
import os
params["url"] = urlparse.urljoin('file:', os.path.abspath("shp.xml"))
message = {}
message["samp.mtype"] = "table.load.votable"
message["samp.params"] = params
client.notify_all(message)
client.disconnect()
## disconnect client, otherwise HUB gets confused
print "table sent"
