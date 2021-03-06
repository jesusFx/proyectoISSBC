#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: ckVTSValoracion
Descripcion: Vistas del sistema
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 07/06/2018
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
        

        #Etiquetas
        self.labelTableWidgetCaso=QtGui.QLabel(u"Casos a valorar", self)
        self.labelListDominios=QtGui.QLabel(u"Dominio",self)
        self.labelListValoraciones=QtGui.QLabel(u"Tipo de valoración",self)
        self.labelListCriterios=QtGui.QLabel(u"Criterios que usa el sistema",self)
        self.labelTextDescripcionCriterio=QtGui.QLabel(u"Descripcion del criterio seleccionado", self)
        self.labelTextjustificacionL=QtGui.QLabel(u"Justificación de la valoración", self)
        self.labelTextResultado=QtGui.QLabel(u"Resultado final")
        self.labelTextDecision=QtGui.QLabel(u" ",self)
        
        #Lista de dominios
        self.listWidgetDominios = QtGui.QComboBox()
        self.dominio = ec.dominios
        if self.dominio is not None:
            self.listWidgetDominios.addItems(self.dominio)

        
        #Tabla para caso
        self.header = ['ATRIBUTO', 'VALOR', 'APLICA A']
        self.tableWidgetCaso = QtGui.QTableWidget(len(self.caso.caracteristicas),3) #Crea la tabla de elementos observables de tres columnas
        self.tableWidgetCaso.setColumnWidth(0, 160) #Asignan ancho a la columna izquierda
        self.tableWidgetCaso.setColumnWidth(1, 124) #Asignan ancho a la columna central
        self.tableWidgetCaso.setColumnWidth(2, 124) #Asignan ancho a la columna derecha
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
                
            item3 = QtGui.QTableWidgetItem(at.aplica)
            item3.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) 
            self.tableWidgetCaso.setItem(i, 2, item3)
            
            i+=1
        
        #Lista de valoraciones
        if self.dom.valoraciones[0] == '':
            pass
        else:
            self.listWidgetValoraciones = QtGui.QComboBox()
            self.valoraciones = self.dom.valoraciones
            if self.valoraciones is not None:
                self.listWidgetValoraciones.addItems(self.valoraciones)
                
            for val in self.valoraciones:
                if self.valoraciones.index(val) == 0:
                    self.privaloracion = val
        
        #Tabla para descripcion criterio
        self.dcriterios = self.dom.criterios(self.valoraciones[0]) #Inicia la lista de criterios para la primera valoracion de la lista por defecto
        
        self.header2 = ['TIPO', 'VALOR']
        self.nombreDescriptores = [u'Nombre',u'Comparación',u'Tipo de resultado',u'Puntuación',u'Valor',u'Terminal'] #Descriptores de la primera columna
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
        
            '''Asignacion de valores a la columna derecha'''
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
        
        #Lista de criterios (usada durante el resto del proceso de valoracion y justificacion)
        self.listWidgetCriterios = QtGui.QListWidget()
        self.dom.valoracionActual = self.valoraciones[0]
        self.cri = self.dom.criterios(self.valoraciones[0])
        if self.cri is not None:
            stringList = []
            for c in self.cri.lcriterios:
                stringList.append(c.nombre)

            self.listWidgetCriterios.addItems(stringList)
            self.listWidgetCriterios.setCurrentRow(0)
            
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

        grid.addWidget(self.labelTableWidgetCaso, 2,0)
        grid.addWidget(self.tableWidgetCaso, 3, 0)

        grid.addWidget(self.labelListCriterios, 4,0)
        grid.addWidget(self.listWidgetCriterios, 5,0)
        
        grid.addWidget(self.labelListValoraciones, 0,1)
        grid.addWidget(self.listWidgetValoraciones, 1,1)
        
        grid.addWidget(self.labelTextResultado, 2,1)
        grid.addWidget(self.plainTextEditResultado, 3,1,1,1)
        
        grid.addWidget(self.labelTextDescripcionCriterio, 4,1)
        grid.addWidget(self.tableWidgetDCriterio, 5,1)

        grid.addWidget(self.labelTextjustificacionL, 0, 2)
        grid.addWidget(self.plainTextEditExplicacion, 1, 2, 5, 1) #Fila, columna, profundidad del plainText, profundidad lateral del plainText

        #Diseño principal
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.btnsLayout)
        self.setLayout(mainLayout)

        #Geometría de la ventana emergente
        self.setGeometry(300, 300, 1100, 600)
        self.setWindowTitle(u"Sistema de valoración")
        self.center()
        self.show()

        #Conexiones al pulsar sobre botones o filas en las listas con las funciones que activan
        self.listWidgetValoraciones.activated[str].connect(self.changeValoracion)
        self.listWidgetDominios.activated[str].connect(self.changeDominio)
        self.listWidgetCriterios.itemClicked.connect(self.showCriterio)
        self.valorarBtn.clicked.connect(self.valorar)
        self.borrarBtn.clicked.connect(self.borrar)
        self.salirBtn.clicked.connect(self.close)

        #Para que comience mostrando la descripcion del primer criterio en el apartado de descripcion de criterio
        self.showCriterio()

    def center(self):
        '''Centrado de los elementos en pantalla en el espacio de ventana disponible'''
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
        '''Muestra la tabla de descripcion de cada criterio'''
        row = self.listWidgetCriterios.currentRow()
        
        #Borra la descripcion de criterio actual
        while self.tableWidgetDCriterio.rowCount() > 0: 
            self.tableWidgetDCriterio.removeRow(0)
        
        #Reinserta las filas de los diferentes atributos de criterio
        while self.tableWidgetDCriterio.rowCount() < len(self.nombreDescriptores):
            self.tableWidgetDCriterio.insertRow(0)
        
        i=0
        cadena = ''
        for at2 in self.dcriterios.lcriterios:
            '''Asignacion de valores a la columna izquierda'''

            for l in self.nombreDescriptores:
                if self.nombreDescriptores.index(l) == i:
                    item3 = QtGui.QTableWidgetItem(l) 
                    item3.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) 
                    self.tableWidgetDCriterio.setItem(i, 0, item3) 
            
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
        self.plainTextEditExplicacion.clear()
        self.plainTextEditResultado.clear()
        
    def changeDominio(self,text):
        '''Cambia la informacion de los casos, los criterios y su descripcion segun el dominio, limpia el resultado y la justificacion'''
        if text != ec.dominioActual:      
            
            #Limpiamos los datos de la interfaz del anterior dominio
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
                item1 = QtGui.QTableWidgetItem(at.atributo.nombre) 
                item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) 
    
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
                    
                item3 = QtGui.QTableWidgetItem(at.aplica) 
                item3.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) 
                self.tableWidgetCaso.setItem(i, 2, item3)
                i+=1
                
            #Tabla para descripcion criterio
            if self.valoraciones is not None:
                self.dcriterios = self.dom.criterios(self.valoraciones[0])
            else:
                self.dcriterios = self.dom.criterios([])
            self.tableWidgetDCriterio.setRowCount(len(self.nombreDescriptores))
    
            i=0
            cadena = ''
            for at2 in self.dcriterios.lcriterios:
                '''Asignacion de valores a la columna izquierda'''
    
                for l in self.nombreDescriptores:
                    if self.nombreDescriptores.index(l) == i:
                        item3 = QtGui.QTableWidgetItem(l)
                        item3.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) 
                        self.tableWidgetDCriterio.setItem(i, 0, item3) 
            
                
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
            elif self.valoraciones[0] == '':
                self.listWidgetValoraciones.addItems(self.valoraciones)
            
            if self.valoraciones is not None:
                self.cri = self.dom.criterios(self.valoraciones[0])
            else:
                self.cri = None
            
            if self.cri is not None:
                stringList = []
                for c in self.cri.lcriterios:
                    stringList.append(c.nombre)
    
                self.listWidgetCriterios.addItems(stringList)
                self.listWidgetCriterios.setCurrentRow(0)


    def changeValoracion(self,text):
        '''Cambia la informacion de los casos, los criterios y su descripcion segun la valoracion en un dominio, limpia el resultado y la justificacion'''
        if text != self.dom.valoracionActual:
            self.listWidgetCriterios.clear()
            self.plainTextEditExplicacion.clear()
            self.plainTextEditResultado.clear()
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
                        item3 = QtGui.QTableWidgetItem(l) 
                        item3.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) 
                        self.tableWidgetDCriterio.setItem(i, 0, item3) 
            
                
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