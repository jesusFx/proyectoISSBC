#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: ckVTSValoracion
Descripcion: Vistas del sistema
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 05/06/2018
"""

from PyQt4 import QtCore
from PyQt4 import QtGui
import ckCtrlValoracion as ctrl
import esqConocimiento as ec


class ValoracionDlg(QtGui.QWidget):
    def __init__(self, caso = None, val = ''):
        super(ValoracionDlg, self).__init__()
        self.dom = ctrl.ma.devolverDominio()
        self.caso = self.dom.inicializarCaso()
        

        #Labels
        self.labelTableWidgetCaso=QtGui.QLabel(u"Caso", self)
        self.labelListDominios=QtGui.QLabel(u"Dominio",self)
        self.labelListValoraciones=QtGui.QLabel(u"Tipo de valoración",self)
        self.labelListCriterios=QtGui.QLabel(u"Criterios",self)
        self.labelTextDescripcionCriterio=QtGui.QLabel(u"Descripcion del criterio", self)
        self.labelTextjustificacionL=QtGui.QLabel(u"Justificación de la valoración", self)
        self.labelTextResultado=QtGui.QLabel(u"Resultado final")
        self.labelTextDecision=QtGui.QLabel(u" ",self)
        
        #Lista de dominios
        self.listWidgetDominios = QtGui.QComboBox()
        self.dominio = ec.dominios
        if self.dominio is not None:
            self.listWidgetDominios.addItems(self.dominio)

        
        #Tabla para caso
        self.header = ['ATRIBUTO', 'VALOR']
        self.tableWidgetCaso = QtGui.QTableWidget(len(self.caso.caracteristicas),2) #Crea la tabla de elementos observables de dos columnas
        self.tableWidgetCaso.setColumnWidth(0, 160) #Asignan ancho a las columnas izq
        self.tableWidgetCaso.setColumnWidth(1, 124) #Asignan ancho a las columnas derech
        self.tableWidgetCaso.setHorizontalHeaderLabels(self.header) #Asigna el header a las columnas 
        

        i=0
        for at in self.caso.caracteristicas:
            item1 = QtGui.QTableWidgetItem(at.atributo.nombre) #Crea un item y le asigna el nombre de la observable
            item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) #Establece propiedades a las celdas de la primera columna

            #Establecemos el item en la columna 0
            self.tableWidgetCaso.setItem(i, 0, item1)
            if at.atributo.tipo == 'bool' or at.atributo.tipo == 'opciones' or at.atributo.tipo == 'varios':
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
        self.valoraciones = self.dom.valoraciones
        if self.valoraciones is not None:
            self.listWidgetValoraciones.addItems(self.valoraciones)
            
        for val in self.valoraciones:
            if self.valoraciones.index(val) == 0:
                self.privaloracion = val
        '''''' 
        #Tabla para descripcion criterio
        self.dcriterios = self.dom.criterios(self.valoraciones[0])
        
        self.header2 = ['TIPO', 'VALOR']
        self.nombreDescriptores = [u'Nombre',u'Comparación',u'Tipo de resultado',u'Puntuación',u'Valor',u'Terminal']
        self.tableWidgetDCriterio = QtGui.QTableWidget(len(self.nombreDescriptores),2) #Crea la tabla de elementos observables de dos columnas
        self.tableWidgetDCriterio.setColumnWidth(0, 160) #Asignan ancho a las columnas izq
        self.tableWidgetDCriterio.setColumnWidth(1, 300) #Asignan ancho a las columnas derech
        self.tableWidgetDCriterio.setHorizontalHeaderLabels(self.header2) #Asigna el header a las columnas 
        

        i=0
        cadena = ''
        for at2 in self.dcriterios.lcriterios:
            '''Asignacion de valores a la columna izquierda'''

            for l in self.nombreDescriptores:
                if self.nombreDescriptores.index(l) == i:
                    item3 = QtGui.QTableWidgetItem(l) #Crea un item y le asigna el nombre de la observable
                    item3.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) #Establece propiedades a las celdas de la primera columna
                    self.tableWidgetDCriterio.setItem(i, 0, item3) #Establecemos el item en la columna 0
        
            
            if i == 0:
                item4= QtGui.QTableWidgetItem(at2.nombre)
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(0, 1, item4)
            
                item4= QtGui.QTableWidgetItem(at2.tipoComparacion)
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(1, 1, item4)
            
                item4= QtGui.QTableWidgetItem(at2.tipoResultado)
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(2, 1, item4)
            
                item4= QtGui.QTableWidgetItem(str(at2.puntuacion))
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(3, 1, item4)
            
            
                if isinstance(at2.valor, int):
                    item4= QtGui.QTableWidgetItem(str(at2.valor))
                elif isinstance(at2.valor, str):
                    item4= QtGui.QTableWidgetItem(at2.valor)
                elif isinstance(at2.valor, list):
                    j=0
                    for l2 in at2.valor:
                        if j != 0:
                            cadena += "-"
                        cadena += str(l2)
                        j+=1
                    item4= QtGui.QTableWidgetItem(cadena)
            
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(4, 1, item4)
            
                item4= QtGui.QTableWidgetItem(str(at2.terminal))
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(5, 1, item4)
                    
            i+=1
            cadena = ''
        ''''''
        #Lista de criterios
        self.listWidgetCriterios = QtGui.QListWidget()
        self.dom.valoracionActual = self.valoraciones[0]
        self.cri = self.dom.criterios(self.valoraciones[0])
        if self.cri is not None:
            stringList = []
            for c in self.cri.lcriterios:
                stringList.append(c.nombre)

            self.listWidgetCriterios.addItems(stringList)
            self.listWidgetCriterios.setCurrentRow(0)
            
        #Cuadro de texto de descripcion de la clase
        #self.plainTextEditDescripcionCriterio = QtGui.QPlainTextEdit()
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
        grid.setSpacing(2)
        
        grid.addWidget(self.labelListDominios, 0,0)
        grid.addWidget(self.listWidgetDominios, 1,0)
        
        grid.addWidget(self.labelListValoraciones, 0,1)
        grid.addWidget(self.listWidgetValoraciones, 1,1)

        grid.addWidget(self.labelTableWidgetCaso, 2,0)
        grid.addWidget(self.tableWidgetCaso, 3, 0)

        grid.addWidget(self.labelListCriterios, 4,0)
        grid.addWidget(self.listWidgetCriterios, 5,0)
        
        grid.addWidget(self.labelTextResultado, 2,1)
        grid.addWidget(self.plainTextEditResultado, 3,1,1,1)
        
        grid.addWidget(self.labelTextDescripcionCriterio, 4,1)
        #grid.addWidget(self.plainTextEditDescripcionCriterio, 5,1)
        grid.addWidget(self.tableWidgetDCriterio, 5,1)

        grid.addWidget(self.labelTextjustificacionL, 0, 2)
        grid.addWidget(self.plainTextEditExplicacion, 1, 2, 5, 1)
        
        
        

        #grid.addWidget(self.labelTextDecision, 6, 0, 6, 2)

        #Diseño principal
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.btnsLayout)
        self.setLayout(mainLayout)


        #Geometría de la ventana emergente
        self.setGeometry(300, 300, 1100, 600)
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
            elif self.caso.caracteristicas[i].atributo.tipo == 'opciones' or self.caso.caracteristicas[i].atributo.tipo == 'varios':
                self.caso.caracteristicas[i].valor = self.tableWidgetCaso.cellWidget(i,1).currentText()

    def showCriterio(self):
        row = self.listWidgetCriterios.currentRow()
        #self.plainTextEditDescripcionCriterio.clear()
        #self.plainTextEditDescripcionCriterio.appendPlainText(self.cri.lcriterios[row].descripcion())
        
        #Borra la descripcion de criterio actual
        while self.tableWidgetDCriterio.rowCount() > 0: 
            self.tableWidgetDCriterio.removeRow(0)
        ##self.tableWidgetDCriterio.setItem(i, 1, item4)
        #appendPlainText(self.cri.lcriterios[row].descripcion())
        
        #Reinserta las filas de los diferentes atributos de criterio
        while self.tableWidgetDCriterio.rowCount() < len(self.nombreDescriptores):
            self.tableWidgetDCriterio.insertRow(0)
        
        i=0
        cadena = ''
        for at2 in self.dcriterios.lcriterios:
            '''Asignacion de valores a la columna izquierda'''

            for l in self.nombreDescriptores:
                if self.nombreDescriptores.index(l) == i:
                    item3 = QtGui.QTableWidgetItem(l) #Crea un item y le asigna el nombre de la observable
                    item3.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) #Establece propiedades a las celdas de la primera columna
                    self.tableWidgetDCriterio.setItem(i, 0, item3) #Establecemos el item en la columna 0
        
            
            if i == row:
                item4= QtGui.QTableWidgetItem(at2.nombre)
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(0, 1, item4)
            
                item4= QtGui.QTableWidgetItem(at2.tipoComparacion)
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(1, 1, item4)
            
                item4= QtGui.QTableWidgetItem(at2.tipoResultado)
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(2, 1, item4)
            
                item4= QtGui.QTableWidgetItem(str(at2.puntuacion))
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(3, 1, item4)
            
            
                if isinstance(at2.valor, int):
                    item4= QtGui.QTableWidgetItem(str(at2.valor))
                elif isinstance(at2.valor, str):
                    item4= QtGui.QTableWidgetItem(at2.valor)
                elif isinstance(at2.valor, list):
                    j=0
                    for l2 in at2.valor:
                        if j != 0:
                            cadena += "-"
                        cadena += str(l2)
                        j+=1
                    item4= QtGui.QTableWidgetItem(cadena)
            
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(4, 1, item4)
            
                item4= QtGui.QTableWidgetItem(str(at2.terminal))
                item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidgetDCriterio.setItem(5, 1, item4)
                    
            i+=1
            cadena = ''

    #Funcion que invoca la valoracion de criterios
    def valorar(self):
        print '\nValorar btn...'
        self.recogerDatos()
        ctrl.eventValorar(self)
    
    #Funcion que borra por pantalla
    def borrar(self):
        #self.plainTextEditDescripcionCriterio.clear()
        self.plainTextEditExplicacion.clear()
        self.plainTextEditResultado.clear()
        
    def changeDominio(self,text):
        if text != ec.dominioActual:            
            #Limpiamos los datos de la interfaz del anterior dominio
            #self.plainTextEditDescripcionCriterio.clear()
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
            self.dom = ctrl.ma.devolverDominio()
            self.caso = self.dom.inicializarCaso()
            self.valoraciones = self.dom.valoraciones
            
            
            self.tableWidgetCaso.setRowCount(len(self.caso.caracteristicas))
            
            i=0
            for at in self.caso.caracteristicas:
                item1 = QtGui.QTableWidgetItem(at.atributo.nombre) #Crea un item y le asigna el nombre de la observable
                item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) #Establece propiedades a las celdas de la primera columna
    
                #Establecemos el item en la columna 0
                self.tableWidgetCaso.setItem(i, 0, item1)
                if at.atributo.tipo == 'bool' or at.atributo.tipo == 'opciones' or at.atributo.tipo == 'varios':
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
                
            #Tabla para descripcion criterio
            self.dcriterios = self.dom.criterios(self.valoraciones[0])
            self.tableWidgetDCriterio.setRowCount(len(self.nombreDescriptores))
    
            i=0
            cadena = ''
            for at2 in self.dcriterios.lcriterios:
                '''Asignacion de valores a la columna izquierda'''
    
                for l in self.nombreDescriptores:
                    if self.nombreDescriptores.index(l) == i:
                        item3 = QtGui.QTableWidgetItem(l) #Crea un item y le asigna el nombre de la observable
                        item3.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) #Establece propiedades a las celdas de la primera columna
                        self.tableWidgetDCriterio.setItem(i, 0, item3) #Establecemos el item en la columna 0
            
                
                if i == 0:
                    item4= QtGui.QTableWidgetItem(at2.nombre)
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(0, 1, item4)
                
                    item4= QtGui.QTableWidgetItem(at2.tipoComparacion)
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(1, 1, item4)
                
                    item4= QtGui.QTableWidgetItem(at2.tipoResultado)
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(2, 1, item4)
                
                    item4= QtGui.QTableWidgetItem(str(at2.puntuacion))
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(3, 1, item4)
                
                
                    if isinstance(at2.valor, int):
                        item4= QtGui.QTableWidgetItem(str(at2.valor))
                    elif isinstance(at2.valor, str):
                        item4= QtGui.QTableWidgetItem(at2.valor)
                    elif isinstance(at2.valor, list):
                        j=0
                        for l2 in at2.valor:
                            if j != 0:
                                cadena += "-"
                            cadena += str(l2)
                            j+=1
                        item4= QtGui.QTableWidgetItem(cadena)
                
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(4, 1, item4)
                
                    item4= QtGui.QTableWidgetItem(str(at2.terminal))
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(5, 1, item4)
                        
                i+=1
                cadena = ''
            
            if self.valoraciones is not None:
                self.listWidgetValoraciones.addItems(self.valoraciones)
                
            self.cri = self.dom.criterios(self.valoraciones[0])
            
            if self.cri is not None:
                stringList = []
                for c in self.cri.lcriterios:
                    stringList.append(c.nombre)
    
                self.listWidgetCriterios.addItems(stringList)
                self.listWidgetCriterios.setCurrentRow(0)


    def changeValoracion(self,text):
        if text != self.dom.valoracionActual:
            #self.plainTextEditDescripcionCriterio.clear()
            self.listWidgetCriterios.clear()
            self.dom.valoracionActual = text
            self.cri = self.dom.criterios(text)
            if self.cri is not None:
                stringList = []
                for c in self.cri.lcriterios:
                    stringList.append(c.nombre)
    
                self.listWidgetCriterios.addItems(stringList)
                self.listWidgetCriterios.setCurrentRow(0)
                
            
            #Tabla para descripcion criterio
            self.dcriterios = self.dom.criterios(text)
            self.tableWidgetDCriterio.setRowCount(len(self.nombreDescriptores))
    
            i=0
            cadena = ''
            for at2 in self.dcriterios.lcriterios:
                '''Asignacion de valores a la columna izquierda'''
    
                for l in self.nombreDescriptores:
                    if self.nombreDescriptores.index(l) == i:
                        item3 = QtGui.QTableWidgetItem(l) #Crea un item y le asigna el nombre de la observable
                        item3.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) #Establece propiedades a las celdas de la primera columna
                        self.tableWidgetDCriterio.setItem(i, 0, item3) #Establecemos el item en la columna 0
            
                
                if i == 0:
                    item4= QtGui.QTableWidgetItem(at2.nombre)
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(0, 1, item4)
                
                    item4= QtGui.QTableWidgetItem(at2.tipoComparacion)
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(1, 1, item4)
                
                    item4= QtGui.QTableWidgetItem(at2.tipoResultado)
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(2, 1, item4)
                
                    item4= QtGui.QTableWidgetItem(str(at2.puntuacion))
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(3, 1, item4)
                
                
                    if isinstance(at2.valor, int):
                        item4= QtGui.QTableWidgetItem(str(at2.valor))
                    elif isinstance(at2.valor, str):
                        item4= QtGui.QTableWidgetItem(at2.valor)
                    elif isinstance(at2.valor, list):
                        j=0
                        for l2 in at2.valor:
                            if j != 0:
                                cadena += "-"
                            cadena += str(l2)
                            j+=1
                        item4= QtGui.QTableWidgetItem(cadena)
                
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(4, 1, item4)
                
                    item4= QtGui.QTableWidgetItem(str(at2.terminal))
                    item4.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidgetDCriterio.setItem(5, 1, item4)
                        
                i+=1
                cadena = ''