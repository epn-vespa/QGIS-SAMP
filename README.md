# VO HUB interface for QGIS
 QGIS-VO_plugin
 connect QGIS to VO HUB

QGIS does not currently connect to VO, or to GAVO. 

The most efficent course of action is to connect QGIS to GAVO via HUB TOPCAT

To do so there needs to be some interface that would allow QGIS to listen to HUB XML-RPC.

This way GAVO can be searched with TOPCAT and results forwarded to QGIS.
Of course, it would be much easier to just have a plugin for QGIS to search GAVO directly 
(perhaps like a day's worth of work) but this is not the best way to do things.

Connecting QGIS to HUB would eliminate the need for GAVO QGIS interface, while also
it will make QGIS part of VO. 

Meaning you can send data from any of the VO tools into QGIS.
Aladin, or CASSIS, or whatever. It's just a "best practices" sorta thing.

So we should probably do it.

This repo is for making a VO HUB interface for QGIS
