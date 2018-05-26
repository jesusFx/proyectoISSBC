#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: appValoracion
Descripcion: Aplicacion principal
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 26/05/2018
"""

import sys
from PyQt4 import QtGui
import ckVtsValoracion as vts

app = QtGui.QApplication(sys.argv)
form = vts.ValoracionDlg()
sys.exit(app.exec_())