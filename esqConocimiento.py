#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: esqConocimiento
Descripcion: Esquema de conocimiento
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 26/05/2018
"""

#Lista de dominios
dominios = ['Erasmus', 'Ejercito']
dominioActual = 'Erasmus'

class Atributo():
    '''Especificamos las propiedades de los atributos que van a usarse
       en la base de conocimiento para describir un caso'''
    def __init__(self,nombre,tipo,unidad,posiblesValores=None):
        self.nombre  =nombre #nombre
        self.tipo = tipo #tipo de atributo
        self.unidad = unidad #unidad(si no la contemplamos)
        if(tipo == 'bool'): #BOOLEANOS
            self.posiblesValores = ['True','False']
        elif(tipo == 'multiple'): #Multiple eleccion
            self.posiblesValores = posiblesValores


class Caracteristica():
    '''Almacena el valor de un atributo'''
    def __init__(self,atributo,valor):
        self.atributo = atributo
        self.valor = valor


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
        self.nombre = nombre #nombre del criterio
        self.atributo = atributo #atributo
        self.tipoComparacion = tipoComparacion #igual, mayor, menor, rango
        self.tipoResultado = tipoResultado #unidad del atributo
        self.puntuacion = puntuacion #los puntos que da al ser aceptado
        self.valor = valor #valor que debe tener el atributo para que se cumpla el criterio.
                           #a puede ser una tupla para una comparación tipo rango
        self.terminal = terminal #si la condicion tiene que ser cumplida obligatoriamente
    def descripcion(self):
        '''Describimos el criterio en el panel del programa'''
        self.desc = u'Nombre:\t\t' + self.nombre  + u'\nComparación:\t' + self.tipoComparacion
        self.desc+=  u'\nTipo de resultado:\t'+str(self.tipoResultado)  
        self.desc += u'\nPuntuación:\t' + str(self.puntuacion) + u'\nValor:\t\t'
        self.desc += str(self.valor) + u'\nTerminal:\t\t' + str(self.terminal)
        return self.desc


class Criterios():
    #Lista de criterios
    def __init__(self, nombre, pnecesario = 60):
        self.nombre = nombre
        self.lcriterios = [] #Lista de los criterios del caso
        self.pnecesario = pnecesario #porcentaje necesario para aceptar el caso
    def append(self, criterio):
        '''Anade un nuevo criterio definido segun el conocimiento'''
        self.lcriterios.append(criterio)
    def puntuacionmax(self):
        '''Retorna la puntuación al sumar el resultado de todos los criterios'''
        self.pmax = 0
        for criterio in self.lcriterios: #recorremos la lista de criterios
            print 'criterio: ', criterio.nombre
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