The following packages must be installed for this to work, use pip:
astropy, PyQt4, resources, os, threading, time, qgis.core, astropy, shapefile, numpy, tempfile, geojson

Add this plugin to the plugins directory (something like .qgis2/python/plugins) and install it.
The SAMP HUB must be running (it's what the plugin connects to), start HUB it by starting TOPCAT.
Once HUB is running, click the "Connect/Disconnect" button, then broadcast a table using interop services.
The table must have s_region field (contains polygon geometry).

The following MTypes are supported: 
table.load.votable, which listens to votable broadcast (standard means of vo interop communications)
qgis.message, prints out a debug message in the dialog box
qgis.script, executes an arbitrary python script sent from VO.
