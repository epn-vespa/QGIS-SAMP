# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VOScriptReceiver
                                 A QGIS plugin
 VOScriptReceiver
                             -------------------
        begin                : 2016-11-10
        copyright            : (C) 2016 by Mikhail Minin
        email                : m.minin@jacobs-university.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load VOScriptReceiver class from file VOScriptReceiver.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .VOScriptReceiver import VOScriptReceiver
    return VOScriptReceiver(iface)
