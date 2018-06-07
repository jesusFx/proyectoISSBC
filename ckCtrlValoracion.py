#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: ckCtrlValoracion
Descripcion: Controlador del sistema
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 07/06/2018
"""

from PyQt4 import QtGui


import ckModValoracion as ma

def eventValorar(ValoracionDlg):
    v = ma.MetodoValoracion(ValoracionDlg.caso)
    d = v.execute()
    ValoracionDlg.plainTextEditExplicacion.clear()
    ValoracionDlg.plainTextEditExplicacion.appendPlainText(d.explain())
    ValoracionDlg.plainTextEditExplicacion.moveCursor(QtGui.QTextCursor.Start)
    ValoracionDlg.plainTextEditResultado.clear()
    resultado = ''
    data = u"+Puntuación máxima -> " + str(v.pmaxima) + "\n" + u"+Puntuación conseguida -> " + str(v.resultados.show()) + "\n" + u"+Porcentaje necesario -> " + str(v.pnecesario) + "\n" + u"+Porcentaje conseguido -> " + str(v.resultados.show() * 100 / v.pmaxima)
    if(d.decision == 0 or d.decision == -1):
        resultado = u"CASO RECHAZADO\n"
        ValoracionDlg.plainTextEditResultado.setStyleSheet("QPlainTextEdit{color:red}")
    else:
        resultado = u"CASO ACEPTADO\n"
        ValoracionDlg.plainTextEditResultado.setStyleSheet("QPlainTextEdit{color:green}")
    ValoracionDlg.plainTextEditResultado.appendPlainText(resultado+data)
    ValoracionDlg.plainTextEditResultado.moveCursor(QtGui.QTextCursor.Start)
    return
