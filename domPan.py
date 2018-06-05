#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nombre: domPan
Descripcion: Fichero de dominio sobre el pan común
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 05/06/2018
"""
import esqConocimiento as ec

#Lista de Valoraciones
valoraciones = ['Pan'] #Valoración por defecto, en este caso no se usa para la valoración del dominio
valoracionActual = ''

def inicializarCaso():
    harina=ec.Caracteristica(Harina(),100)
    agua=ec.Caracteristica(Agua(),55)
    levadura=ec.Caracteristica(Levadura(),4)
    mejorante=ec.Caracteristica(Mejorante(), 'No')
    masaM=ec.Caracteristica(MasaMadre(),20)
    salY=ec.Caracteristica(Sal(),2)
    fermentacion=ec.Caracteristica(Fermentacion(),70)
    horno=ec.Caracteristica(Horno(),220)
    coccion=ec.Caracteristica(Coccion(),35)
    solicitud=ec.Caso([harina,agua,levadura,mejorante,masaM,salY,fermentacion,horno,coccion])
    return solicitud

#Elementos del dominio sobre prestamos
class Harina(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Harina trigo (kg)','int',None,'estado')
class Agua(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Agua (l)','int',None,'estado')
class Levadura(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Levadura (kg)','int',None,'estado')
class Mejorante(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Uso mejorantes','varios',None, ['No','Si'])
class MasaMadre(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Masa madre (kg)','int',None,'estado')
class Sal(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Sal (kg)','int',None,'estado')
class Fermentacion(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Tiempo fermentacion (min)','int',None,'estado')
class Horno(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Temperatura horno (centig)','int',None, 'estado')
class Coccion(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Tiempo coccion (min)','int',None, 'estado')


def criterios(valoracion):
    criterios = []
    
    crt1=ec.Criterio('Harina [95-105]: peso (kg)', Harina(), 'rango', 'estado', 15, [95,105], True)
    crt2=ec.Criterio('Agua [53-57]: capacidad (l)', Agua(),'rango', 'estado', 15, [53,57], True)       
    crt3=ec.Criterio('Levadura [3-5]: peso (kg)', Levadura(), 'rango', 'estado', 15, [3,5], True)
    crt4=ec.Criterio('Mejorante: peso', Mejorante(), 'categorica', None, 10, ['Si'], False)
    crt5=ec.Criterio('Masa madre [19-21]: peso (kg)', MasaMadre(), 'rango', 'puntos', 15, [19,21], True)
    crt6=ec.Criterio('Sal [1-3]: peso (kg)', Sal(), 'rango', 'estado', 15, [1,3], True)
    crt7=ec.Criterio('Fermentacion [60-80]: tiempo (min)', Fermentacion(), 'rango', 'estado', 15, [60,80], True)
    crt8=ec.Criterio('Horno [200-250]: temperatura (centig)', Horno(), 'rango', 'estado', 15, [200,250], True)
    crt9=ec.Criterio('Coccion [25-45]: tiempo (min)', Coccion(), 'rango', 'estado', 15, [25,45], True)
    criterios=ec.Criterios('Criterios de estado del pan', 50)
   
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