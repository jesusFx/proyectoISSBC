#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nombre: domPan
Descripcion: Fichero de dominio sobre el pan común
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 07/06/2018
"""
import esqConocimiento as ec

#Lista de Valoraciones
valoraciones = ['Pan'] #Valoración por defecto, en este caso no se usa para la valoración del dominio
valoracionActual = ''

def inicializarCaso():
    harina=ec.Caracteristica(Harina(),100, 'Pan')
    agua=ec.Caracteristica(Agua(),55, 'Pan')
    levadura=ec.Caracteristica(Levadura(),4, 'Pan')
    mejorante=ec.Caracteristica(Mejorante(), 'No', 'Pan')
    masaM=ec.Caracteristica(MasaMadre(),20, 'Pan')
    salY=ec.Caracteristica(Sal(),2, 'Pan')
    fermentacion=ec.Caracteristica(Fermentacion(),70, 'Pan')
    horno=ec.Caracteristica(Horno(),220, 'Pan')
    coccion=ec.Caracteristica(Coccion(),35, 'Pan')
    
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
    
    crt1=ec.Criterio('Harina [90-110]: peso (kg)', Harina(), 'rango', 'puntos', 5, [90,110], True)
    crt2=ec.Criterio('Harina [95-105]: peso (kg)', Harina(), 'rango', 'puntos', 15, [95,105], False)
    crt3=ec.Criterio('Agua [49-62]: capacidad (l)', Agua(),'rango', 'puntos', 5, [49,62], True)
    crt4=ec.Criterio('Agua [53-57]: capacidad (l)', Agua(),'rango', 'puntos', 15, [53,57], False)  
    crt5=ec.Criterio('Levadura [1-7]: peso (kg)', Levadura(), 'rango', 'puntos', 5, [1,7], True)     
    crt6=ec.Criterio('Levadura [3-5]: peso (kg)', Levadura(), 'rango', 'puntos', 20, [3,5], False)
    crt7=ec.Criterio('Mejorante [No]: peso', Mejorante(), 'categorica', 'puntos', 0, ['No'], False)
    crt8=ec.Criterio('Mejorante [Si]: peso', Mejorante(), 'categorica', 'puntos', 20, ['Si'], False)
    crt9=ec.Criterio('Masa madre [16-24]: peso (kg)', MasaMadre(), 'rango', 'puntos', 5, [16,24], True)
    crt10=ec.Criterio('Masa madre [19-21]: peso (kg)', MasaMadre(), 'rango', 'puntos', 10, [19,21], False)
    crt11=ec.Criterio('Sal [1-3]: peso (kg)', Sal(), 'rango', 'puntos', 10, [1,3], True)
    crt12=ec.Criterio('Fermentacion [56-84]: tiempo (min)', Fermentacion(), 'rango', 'puntos', 5, [56,84], True)
    crt13=ec.Criterio('Fermentacion [60-80]: tiempo (min)', Fermentacion(), 'rango', 'puntos', 15, [60,80], False)
    crt14=ec.Criterio('Horno [200-250]: temperatura (centig)', Horno(), 'rango', 'puntos', 15, [200,250], True)
    crt15=ec.Criterio('Coccion [25-45]: tiempo (min)', Coccion(), 'rango', 'puntos', 15, [25,45], True)
    criterios=ec.Criterios('Criterios de estado del pan', 80, 15)
   
    criterios.append(crt1)
    criterios.append(crt2)
    criterios.append(crt3)
    criterios.append(crt4)
    criterios.append(crt5)
    criterios.append(crt6)
    criterios.append(crt7)
    criterios.append(crt8)
    criterios.append(crt9)
    criterios.append(crt10)
    criterios.append(crt11)
    criterios.append(crt12)
    criterios.append(crt13)
    criterios.append(crt14)
    criterios.append(crt15)
        
    return criterios