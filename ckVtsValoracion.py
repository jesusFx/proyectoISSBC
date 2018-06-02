#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: ckVTSValoracion
Descripcion: Vistas del sistema
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 26/05/2018
"""

from PyQt4 import QtCore
from PyQt4 import QtGui
import ckCtrlValoracion as ctrl
import esqConocimiento as ec


class ValoracionDlg(QtGui.QWidget):
    def __init__(self, caso = None):
        super(ValoracionDlg, self).__init__()
        self.cd = ctrl.ma.devolverDominio()
        self.caso = self.cd.inicializarCaso()
        

        #Labels
        self.labelTableWidgetCaso=QtGui.QLabel(u"Caso", self)
        self.labelListDominios=QtGui.QLabel(u"Dominio",self)
        self.labelListValoraciones=QtGui.QLabel(u"Valoracion",self)
        self.labelListCriterios=QtGui.QLabel(u"Criterios",self)
        self.labelTextDescripcionCriterio=QtGui.QLabel(u"Descripcion del criterio", self)
        self.labelTextjustificacionL=QtGui.QLabel(u"Justificación de la valoración", self)
        self.labelTextResultado=QtGui.QLabel(u"Resultado Final")
        self.labelTextDecision=QtGui.QLabel(u" ",self)
        
        #Lista de dominios
        self.listWidgetDominios = QtGui.QComboBox()
        self.dominio = ec.dominios
        if self.dominio is not None:
            self.listWidgetDominios.addItems(self.dominio)

        #Table
        self.header = ['ATRIBUTO', 'VALOR']
        self.tableWidgetCaso = QtGui.QTableWidget(len(self.caso.caracteristicas),2) #Crea la tabla de elementos observables de dos columnas
        self.tableWidgetCaso.setColumnWidth(0, 225) #Asignan ancho a las columnas izq
        self.tableWidgetCaso.setColumnWidth(1, 225) #Asignan ancho a las columnas derech
        self.tableWidgetCaso.setHorizontalHeaderLabels(self.header) #Asigna el header a las columnas

        i=0
        for at in self.caso.caracteristicas:
            item1 = QtGui.QTableWidgetItem(at.atributo.nombre) #Crea un item y le asigna el nombre de la observable
            item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) #Establece propiedades a las celdas de la primera columna

            #Establecemos el item en la columna 0
            self.tableWidgetCaso.setItem(i, 0, item1)
            if at.atributo.tipo == 'bool' or at.atributo.tipo == 'opciones':
                item2= QtGui.QComboBox()
                item2.addItems(at.atributo.posiblesValores)
                self.tableWidgetCaso.setCellWidget(i, 1, item2)
            elif isinstance(at.valor, int):
                item2 = QtGui.QTableWidgetItem(str(at.valor))
                self.tableWidgetCaso.setItem(i, 1, item2)
            elif isinstance(at.valor, str):
                item2 = QtGui.QTableWidgetItem(at.valor)
                self.tableWidgetCaso.setItem(i, 1, item2)
            i+=1

        #Lista de valoraciones
        self.listWidgetValoraciones = QtGui.QComboBox()
        self.valoraciones = self.cd.valoraciones
        if self.valoraciones is not None:
            self.listWidgetValoraciones.addItems(self.valoraciones)

        #Lista de criterios
        self.listWidgetCriterios = QtGui.QListWidget()
        self.cd.valoracionActual = self.valoraciones[0]
        self.cri = self.cd.criterios(self.valoraciones[0])
        if self.cri is not None:
            stringList = []
            for c in self.cri.lcriterios:
                stringList.append(c.nombre)

            self.listWidgetCriterios.addItems(stringList)
            self.listWidgetCriterios.setCurrentRow(0)

        #Cuadro de texto de descripcion de la clase
        self.plainTextEditDescripcionCriterio = QtGui.QPlainTextEdit()
        #Cuadro de texto de la explicacion
        self.plainTextEditExplicacion = QtGui.QPlainTextEdit()
        #Cuadro de texto del resultado final
        self.plainTextEditResultado = QtGui.QPlainTextEdit()


        #Buttons
        self.valorarBtn=QtGui.QPushButton('Valorar')
        self.borrarBtn=QtGui.QPushButton('Borrar')
        self.salirBtn=QtGui.QPushButton('Salir')
        self.btnsLayout = QtGui.QHBoxLayout()
        self.btnsLayout.addStretch()
        self.btnsLayout.addWidget(self.valorarBtn)
        self.btnsLayout.addWidget(self.borrarBtn)
        self.btnsLayout.addWidget(self.salirBtn)
        self.btnsLayout.addStretch()

        #Rejilla de distribucion de los controles
        grid = QtGui.QGridLayout()
        grid.setSpacing(3)
        
        grid.addWidget(self.labelListDominios, 0,0)
        grid.addWidget(self.listWidgetDominios, 1, 0)

        grid.addWidget(self.labelTableWidgetCaso, 2,0)
        grid.addWidget(self.tableWidgetCaso, 3, 0)
        
        grid.addWidget(self.labelListValoraciones, 4,0)
        grid.addWidget(self.listWidgetValoraciones, 5,0)

        grid.addWidget(self.labelListCriterios, 6,0)
        grid.addWidget(self.listWidgetCriterios, 7, 0)

        grid.addWidget(self.labelTextDescripcionCriterio, 8,0)
        grid.addWidget(self.plainTextEditDescripcionCriterio, 9, 0)
        
        grid.addWidget(self.labelTextResultado, 0,1)
        grid.addWidget(self.plainTextEditResultado, 1,1,3,1)

        grid.addWidget(self.labelTextjustificacionL, 4, 1)
        grid.addWidget(self.plainTextEditExplicacion, 5, 1, 6,1)
        
        
        

        #grid.addWidget(self.labelTextDecision, 6, 0, 6, 2)

        #Diseno principal
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.btnsLayout)
        self.setLayout(mainLayout)


        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle(u"Tarea de valoración")
        self.center()
        self.show()


        #Conexiones
        self.listWidgetValoraciones.activated[str].connect(self.changeValoracion)
        self.listWidgetDominios.activated[str].connect(self.changeDominio)
        self.listWidgetCriterios.itemClicked.connect(self.showCriterio)
        self.valorarBtn.clicked.connect(self.valorar)
        self.borrarBtn.clicked.connect(self.borrar)
        self.salirBtn.clicked.connect(self.close)

        #Para que comience mostrando el primer criterio en la descripcion
        self.showCriterio()



    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def recogerDatos(self):
        for i in range(self.tableWidgetCaso.rowCount()):
            if self.caso.caracteristicas[i].atributo.tipo == 'str':
                self.caso.caracteristicas[i].valor = self.tableWidgetCaso.item(i,1).text()
            elif self.caso.caracteristicas[i].atributo.tipo == 'int':
                self.caso.caracteristicas[i].valor = int(self.tableWidgetCaso.item(i,1).text())
            elif self.caso.caracteristicas[i].atributo.tipo == 'float':
                self.caso.caracteristicas[i].valor = float(self.tableWidgetCaso.item(i,1).text())
            elif self.caso.caracteristicas[i].atributo.tipo == 'bool':
                if(self.tableWidgetCaso.cellWidget(i,1).currentText()=='True'):
                    self.caso.caracteristicas[i].valor = True
                else:
                    self.caso.caracteristicas[i].valor = False
            elif self.caso.caracteristicas[i].atributo.tipo == 'multiple':
                self.caso.caracteristicas[i].valor = self.tableWidgetCaso.cellWidget(i,1).currentText()


    def showCriterio(self):
        row = self.listWidgetCriterios.currentRow()
        self.plainTextEditDescripcionCriterio.clear()
        self.plainTextEditDescripcionCriterio.appendPlainText(self.cri.lcriterios[row].descripcion())


    def valorar(self):
        print '\nValorar btn...'
        self.recogerDatos()
        ctrl.eventValorar(self)
        
    def borrar(self):
        self.plainTextEditDescripcionCriterio.clear()
        self.plainTextEditExplicacion.clear()
        self.plainTextEditResultado.clear()
        
    def changeDominio(self,text):
        if text != ec.dominioActual:            
            #Limpiamos los datos de la interfaz del anterior dominio
            self.plainTextEditDescripcionCriterio.clear()
            self.plainTextEditExplicacion.clear()
            self.plainTextEditResultado.clear()
            for i in range(len(self.valoraciones)):
                self.listWidgetValoraciones.removeItem(0)
            for i in range(len(self.caso.caracteristicas)):
                self.tableWidgetCaso.removeRow(0)
            for i in range(self.listWidgetCriterios.count()):
                self.listWidgetCriterios.takeItem(0)
            
            #Cambiamos el dominio
            ec.dominioActual = text
            self.cd = ctrl.ma.devolverDominio()
            self.caso = self.cd.inicializarCaso()
            self.valoraciones = self.cd.valoraciones
            
            
            self.tableWidgetCaso.setRowCount(len(self.caso.caracteristicas))
            
            i=0
            for at in self.caso.caracteristicas:
                item1 = QtGui.QTableWidgetItem(at.atributo.nombre) #Crea un item y le asigna el nombre de la observable
                item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) #Establece propiedades a las celdas de la primera columna
    
                #Establecemos el item en la columna 0
                self.tableWidgetCaso.setItem(i, 0, item1)
                if at.atributo.tipo == 'bool' or at.atributo.tipo == 'opciones':
                    item2= QtGui.QComboBox()
                    item2.addItems(at.atributo.posiblesValores)
                    self.tableWidgetCaso.setCellWidget(i, 1, item2)
                elif isinstance(at.valor, int) or isinstance(at.valor, float):
                    item2 = QtGui.QTableWidgetItem(str(at.valor))
                    self.tableWidgetCaso.setItem(i, 1, item2)
                elif isinstance(at.valor, str):
                    item2 = QtGui.QTableWidgetItem(at.valor)
                    self.tableWidgetCaso.setItem(i, 1, item2)
                i+=1
            
            if self.valoraciones is not None:
                self.listWidgetValoraciones.addItems(self.valoraciones)
                
            self.cri = self.cd.criterios(self.valoraciones[0])
            
            if self.cri is not None:
                stringList = []
                for c in self.cri.lcriterios:
                    stringList.append(c.nombre)
    
                self.listWidgetCriterios.addItems(stringList)
                self.listWidgetCriterios.setCurrentRow(0)


    def changeValoracion(self,text):
        if text != self.cd.valoracionActual:
            self.plainTextEditDescripcionCriterio.clear()
            self.listWidgetCriterios.clear()
            self.cd.valoracionActual = text
            self.cri = self.cd.criterios(text)
            if self.cri is not None:
                stringList = []
                for c in self.cri.lcriterios:
                    stringList.append(c.nombre)
    
                self.listWidgetCriterios.addItems(stringList)
                self.listWidgetCriterios.setCurrentRow(0)