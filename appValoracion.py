#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: appValoracion
Descripcion: Aplicacion principal
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 05/06/2018
"""

import sys
from PyQt4 import QtGui
import ckVtsValoracion as vts

app = QtGui.QApplication(sys.argv)
form = vts.ValoracionDlg()
sys.exit(app.exec_())