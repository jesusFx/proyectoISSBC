#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: esqConocimiento
Descripcion: Esquema de conocimiento
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 07/06/2018
"""

#Lista de dominios
dominios = ['ITV', 'Pan comun']
dominioActual = 'ITV'

class Atributo():
    '''Propiedades de los atributos a usar en la base de conocimiento para describir un caso'''
    def __init__(self,nombre,tipo,unidad,posiblesValores=None):
        self.nombre  =nombre #Nombre del caso
        self.tipo = tipo #Tipo de atributo del caso
        self.unidad = unidad #Unidad(si no la contemplamos)
        if(tipo == 'bool'): #Elementos booleanos
            self.posiblesValores = ['True','False']
        elif(tipo == 'opciones'): #Eleccion de opciones
            self.posiblesValores = ['Correcto','Aceptable','Deteriorado']
        elif(tipo == 'varios'): #Eleccion de varias opciones distintas
            self.posiblesValores = posiblesValores


class Caracteristica():
    '''Almacena el valor de un atributo'''
    def __init__(self,atributo,valor, aplica):
        self.atributo = atributo
        self.valor = valor
        self.aplica = aplica #A qué dominio se aplica


class Caso():
    '''Caso a evaluar, compuesto de una lista de caracteristicas'''
    def __init__(self,caracteristicas):
        self.caracteristicas = caracteristicas
    def descripcion(self):
        print "\nCaracterísticas del caso:"
        for i in self.caracteristicas:
            print i.atributo.nombre, i.valor
        print ' '


class Criterio():
    '''Establece un criterio a evaluar'''
    def __init__(self,nombre,atributo,tipoComparacion,tipoResultado,
                 puntuacion,valor,terminal):
        self.nombre = nombre #Nombre del criterio
        self.atributo = atributo #Atributo
        self.tipoComparacion = tipoComparacion #Igual, distinto, mayor, menor, rango, categorica
        self.tipoResultado = tipoResultado #Unidad del atributo
        self.puntuacion = puntuacion #Los puntos que da al ser aceptado
        self.valor = valor #Valor que debe tener el atributo para que se cumpla el criterio,
                           #puede ser una tupla para una comparación tipo rango
        self.terminal = terminal #Si la condicion tiene que ser cumplida obligatoriamente
    def descripcion(self):
        '''Describimos el criterio en el panel del programa'''
        self.desc = u'Nombre:\t\t' + self.nombre  + u'\nComparación:\t' + self.tipoComparacion
        self.desc+=  u'\nTipo de resultado:\t'+str(self.tipoResultado)  
        self.desc += u'\nPuntuación:\t' + str(self.puntuacion) + u'\nValor:\t\t'
        self.desc += str(self.valor) + u'\nTerminal:\t\t' + str(self.terminal)
        return self.desc


class Criterios():
    #Lista de criterios
    def __init__(self, nombre, pnecesario = 60, ncriterios = 0):
        self.nombre = nombre
        self.lcriterios = [] #Lista de los criterios del caso
        self.pnecesario = pnecesario #Porcentaje necesario para aceptar el caso
        self.ncriterios = ncriterios #Numero de criterios, obliga al sistema a cumplir todos los criterios en caso de ser necesario
    def append(self, criterio):
        '''Anade un nuevo criterio definido segun el conocimiento'''
        self.lcriterios.append(criterio)
    def puntuacionmax(self):
        '''Retorna la puntuación al sumar el resultado de todos los criterios'''
        self.pmax = 0
        for criterio in self.lcriterios: #Recorremos la lista de criterios
            print 'Criterio: ', criterio.nombre
            self.pmax += criterio.puntuacion
        return self.pmax

class Resultados():
    '''Resultados de criterios evaluados'''
    def __init__(self):
        self.lresultados = []
    def append(self, valor):
        self.lresultados.append(valor)
    def show(self):
        self.puntos = 0
        for valor in self.lresultados:
            if(valor.puntuacion > 0):
                self.puntos += valor.puntuacion
        return self.puntos


class Valor():
    '''Valor que devuelve la inferencia Evaluar'''
    def __init__(self, criterio, caso, puntuacion):
        self.criterio = criterio
        self.caso = caso
        self.puntuacion = puntuacion

class Decision():
    '''-1 para rechazar, 0 para seguir, 1 para aceptar. Contiene el veredicto y la explicacion'''
    def __init__(self, decision, explicacion):
        self.decision = decision
        self.explicacion = explicacion
    def addexp(self, explicacion):
        self.explicacion = explicacion
    def explain(self):
        return self.explicacion