#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: domITV
Descripcion: Fichero de dominio de vehículos de ITV
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 26/05/2018
"""

import esqConocimiento as ec

#Lista de Valoraciones
valoraciones = ['Coche','Motocicleta']
valoracionActual = ''

def inicializarCaso():
    edad=ec.Caracteristica(Edad(),20)
    medico=ec.Caracteristica(Medico(),True)
    psicotecnico=ec.Caracteristica(Psicotecnico(), True)
    nFisico=ec.Caracteristica(Fisico(), 10)
    nTeroria=ec.Caracteristica(Teoria(), 8)
    solicitud=ec.Caso([edad,medico,psicotecnico,nFisico,nTeroria])
    return solicitud

#Elementos del dominio sobre prestamos
class Edad(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Edad','int','ayo')
class Medico(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Test Medico','bool',None)
class Psicotecnico(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Psicotecnico','bool',None)
class Fisico(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Pruebas Fisicas','int',None,'Puntos')
class Teoria(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Pruebas Teoricas','int',None, 'Puntos')


def criterios(valoracion):
    criterios = []
    if valoracion == 'Coche':
        crt1=ec.Criterio('Edad', Edad(), 'rango', 'ayo', 10, [18,25], True)
        crt2=ec.Criterio('Prueba Medica', Medico(),'igual', None, 10, True, True)       
        crt3=ec.Criterio('Prueba Psicotecnica', Psicotecnico(), 'igual', None, 10, True, True) 
        crt4=ec.Criterio('Nota Pruebas Fisicas[5-8]', Fisico(), 'rango', 'puntos', 30, [5,8], False)
        crt5=ec.Criterio('Nota Pruebas Fisicas[8-10]', Fisico(), 'rango', 'puntos', 50, [8,10], False)
        crt6=ec.Criterio('Nota Teoria[5-7]', Teoria(), 'rango', 'puntos', 20, [5,7], False)
        crt7=ec.Criterio('Nota Teoria[7-8]', Teoria(), 'rango', 'puntos', 30, [7,8], False)
        crt8=ec.Criterio('Nota Teoria[8-10]', Teoria(), 'rango', 'puntos', 50, [8,10], False)
        criterios=ec.Criterios('Criterios de acceso', 30)
       
        criterios.append(crt1)
        criterios.append(crt2)
        criterios.append(crt3)
        criterios.append(crt4)
        criterios.append(crt5)
        criterios.append(crt6)
        criterios.append(crt7)
        criterios.append(crt8)
        
    elif valoracion == 'Motocicleta':
        crt1=ec.Criterio('Edad', Edad(), 'rango', 'ayo', 10, [20,35], True)
        crt2=ec.Criterio('Prueba Medica', Medico(),'igual', None, 10, True, True)       
        crt3=ec.Criterio('Prueba Psicotecnica', Psicotecnico(), 'igual', None, 10, True, True) 
        crt4=ec.Criterio('Nota Pruebas Fisicas[5-8]', Fisico(), 'rango', 'puntos', 30, [5,8], False)
        crt5=ec.Criterio('Nota Pruebas Fisicas[8-10]', Fisico(), 'rango', 'puntos', 50, [8,10], False)
        crt6=ec.Criterio('Nota Teoria[5-7]', Teoria(), 'rango', 'puntos', 20, [5,7], False)
        crt7=ec.Criterio('Nota Teoria[7-8]', Teoria(), 'rango', 'puntos', 30, [7,8], False)
        crt8=ec.Criterio('Nota Teoria[8-10]', Teoria(), 'rango', 'puntos', 50, [8,10], False)
        criterios=ec.Criterios('Criterios de acceso', 50)
       
        criterios.append(crt1)
        criterios.append(crt2)
        criterios.append(crt3)
        criterios.append(crt4)
        criterios.append(crt5)
        criterios.append(crt6)
        criterios.append(crt7)
        criterios.append(crt8) 
        
    return criterios