#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nombre: domPan
Descripcion: Fichero de dominio sobre el pan común
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 26/05/2018
"""
import esqConocimiento as ec

#Lista de Valoraciones
valoracionActual = ''

def inicializarCaso():
    edad=ec.Caracteristica(Edad(),20)
    creditos=ec.Caracteristica(Creditos(),161)
    notaMedia=ec.Caracteristica(Media(), 9)
    nivelIngles=ec.Caracteristica(Ingles(), 'B2')
    solicitud=ec.Caso([edad,creditos,notaMedia,nivelIngles])
    return solicitud

#Elementos del dominio sobre prestamos
class Edad(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Edad','int','ayo')
class Creditos(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Creditos aprobados','int',None,'creditos')
class Media(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Nota media','int','puntos')
class Ingles(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Nivel de ingles','multiple',None, ['B1','B2','C1','C2'])


def criterios(valoracion):
    criterios = []
    
    crt1=ec.Criterio('Edad', Edad(), 'rango', 'ayo', 10, [18,26], True)
    crt2=ec.Criterio('Creditos aprobados[60-227]', Creditos(),'rango', 'creditos', 30, [60,227], True)       
    crt3=ec.Criterio('Nota media[5-7]', Media(), 'rango', 'puntos', 20, [5,7], False)
    crt4=ec.Criterio('Nota media[7-8]', Media(), 'rango', 'puntos', 30, [7,8], False)
    crt5=ec.Criterio('Nota media[8-10]', Media(), 'rango', 'puntos', 50, [8,10], False)
    crt6=ec.Criterio('Nivel de ingles-B1', Ingles(), 'categorica', None, 5, ['B1',],False)
    crt7=ec.Criterio('Nivel de ingles-B2', Ingles(), 'categorica', None, 10, ['B2'],False)
    crt8=ec.Criterio('Nivel de ingles-C1', Ingles(), 'categorica', None, 20, ['C1'],False)
    crt9=ec.Criterio('Nivel de ingles-C2', Ingles(), 'categorica', None, 30, ['C2'],False)
    criterios=ec.Criterios('Criterios de la Beca', 30)
   
    criterios.append(crt1)
    criterios.append(crt2)
    criterios.append(crt3)
    criterios.append(crt4)
    criterios.append(crt5)
    criterios.append(crt6)
    criterios.append(crt7)
    criterios.append(crt8)
    criterios.append(crt9)
        
    return criterios