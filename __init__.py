# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SDB
                                 A QGIS plugin
 Satellite derived bathymetry
                             -------------------
        begin                : 2016-06-28
        copyright            : (C) 2016 by SPC /  Herve and Cyprien
        email                : herveda@spc.int;cyprienb@spc.int
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
    """Load SDB class from file SDB.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .SDB import SDB
    return SDB(iface)
