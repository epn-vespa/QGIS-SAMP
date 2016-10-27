# VO HUB interface for QGIS
 QGIS-VO_plugin
 connect QGIS to VO HUB

QGIS does not currently connect to VO, or to GAVO. 

The most efficent course of action is to connect QGIS to GAVO via HUB TOPCAT

To do so there needs to be some interface that would allow QGIS to listen to HUB XML-RPC.

This way GAVO can be searched with TOPCAT and results forwarded to QGIS.
(It is also possible to search GAVO directly, but TOPCAT is better suited for this.)

Connecting QGIS to HUB would eliminate the need for GAVO QGIS interface, while also
it will make QGIS part of VO. 

This way data from any of the VO tools (Aladin, CASSIS, etc.) can be sent to QGIS with interop services.

This repo is for making a VO HUB interface for QGIS using primarily astropy.vo.samp module.
