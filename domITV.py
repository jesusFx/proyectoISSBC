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

#Tabla de casos a valorar, junto con sus valores iniciales (editable para dinamizar el sistema)
def inicializarCaso():
    documentacion=ec.Caracteristica(Documentacion(),1)
    frenos=ec.Caracteristica(Frenos(),'Correcto')
    interior=ec.Caracteristica(Interior(),'Correcto')
    carroceria=ec.Caracteristica(Carroceria(),'Correcto')
    iluminacion=ec.Caracteristica(Iluminacion(),'Correcto')
    suspension=ec.Caracteristica(Suspension(),3)
    emisiones=ec.Caracteristica(Emisiones(),0)
    niveles=ec.Caracteristica(Niveles(),4)
    neumaticos=ec.Caracteristica(Neumaticos(),3)
    motor=ec.Caracteristica(Motor(),2)
    
    solicitud=ec.Caso([documentacion,frenos,interior,carroceria,iluminacion,suspension,emisiones,niveles,neumaticos,motor])
    return solicitud

#Elementos del dominio sobre componentes de un vehículo y sobre la documentación adjunta
class Documentacion(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Documentacion disponible','int',None,'Puntos')
class Frenos(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Estado frenos','opciones',None)
class Interior(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Estado interior','opciones',None)
class Carroceria(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Estado carroceria','opciones',None)
class Iluminacion(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Estado iluminacion','opciones',None)
class Suspension(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Nivel suspension','int',None,'Puntos')
class Emisiones(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Nivel emisiones','int',None,'Puntos')
class Niveles(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Niveles marcados','int',None,'Puntos')
class Neumaticos(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Estado neumaticos','int',None,'Puntos')
class Motor(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Estado motor','int',None,'Puntos')

#Lista de criterios usados en la valoración junto con sus rangos de valores y puntuaciones acordes
def criterios(valoracion):
    criterios = []
    if valoracion == 'Coche':
        crt1=ec.Criterio('Documentacion [1-3]: permiso, tarjeta inspeccion tecnica, comprobante pago seguro', Documentacion(), 'rango', 'puntos', 15, [1,3], True)
        crt2=ec.Criterio('Frenos [Deteriorado][0-1]: Frenada', Frenos(),'igual', None, 0, 'Deteriorado', False)
        crt3=ec.Criterio('Frenos [Aceptable][2-3]', Frenos(),'igual', None, 5, 'Aceptable', False) 
        crt4=ec.Criterio('Frenos [Correcto][4]', Frenos(),'igual', None, 15, 'Correcto', False)    
        crt5=ec.Criterio('Interior [Deteriorado][0-1]: cinturon, ventanillas, asientos, cuadro mandos', Interior(), 'igual', None, 0, 'Deteriorado', False)
        crt6=ec.Criterio('Interior [Aceptable][2]', Interior(), 'igual', None, 5, 'Aceptable', False)  
        crt7=ec.Criterio('Interior [Correcto][3-4]', Interior(), 'igual', None, 15, 'Correcto', False) 
        crt8=ec.Criterio('Carroceria  [Deteriorado][0-2]: puertas, retrovisores, parachoques, legibilidad y visibilidad matricula, guardabarros', Carroceria(), 'igual', None, 0, 'Deteriorado', False)
        crt9=ec.Criterio('Carroceria [Aceptable][3-4]', Carroceria(), 'igual', None, 5, 'Aceptable', False)
        crt10=ec.Criterio('Carroceria [Correcto][5-6]', Carroceria(), 'igual', None, 15, 'Correcto', False)
        crt11=ec.Criterio('Iluminacion [Deteriorado][0-1]: largas, cortas, carretera, antiniebla, intermitentes', Iluminacion(), 'igual', None, 0, 'Deteriorado', False)
        crt12=ec.Criterio('Iluminacion [Aceptable][2-3]', Iluminacion(), 'igual', None, 5, 'Aceptable', False)
        crt13=ec.Criterio('Iluminacion [Correcto][4-5]', Iluminacion(), 'igual', None, 15, 'Correcto', False)
        crt14=ec.Criterio('Suspension [0] [Desfavorable]', Suspension(), 'mayor', 'puntos', 0, 1, True)
        crt15=ec.Criterio('Suspension [1]', Suspension(), 'igual', 'puntos', 5, 1, False)
        crt16=ec.Criterio('Suspension [2]', Suspension(), 'igual', 'puntos', 15, 2, False)
        crt17=ec.Criterio('Emisiones [0] [Bajas]', Emisiones(), 'igual', 'puntos', 15, 0, False)
        crt18=ec.Criterio('Emisiones [1] [Altas]', Emisiones(), 'igual', 'puntos', 5, 1, False)
        crt19=ec.Criterio('Niveles [0-2] [Desfavorable]', Niveles(), 'mayor', 'puntos', 0, 3, True)
        crt20=ec.Criterio('Niveles [3]', Niveles(), 'igual', 'puntos', 5, 3, False)
        crt21=ec.Criterio('Niveles [4-5]', Niveles(), 'rango', 'puntos', 15, [4,5], False)
        crt22=ec.Criterio('Neumaticos [0-2] [Desfavorable]', Neumaticos(), 'mayor', 'puntos', 0, 3, True)
        crt23=ec.Criterio('Neumaticos [3-4] [Nro neumaticos]', Neumaticos(), 'rango', 'puntos', 15, [3,4], False)
        crt24=ec.Criterio('Motor [0-1] [Desfavorable]', Motor(), 'mayor', 'puntos', 0, 2, True)
        crt25=ec.Criterio('Motor [2-3]', Motor(), 'rango', 'puntos', 15, [2,3], False)
        criterios=ec.Criterios('Criterios de acceso', 55)
       
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
        criterios.append(crt16)
        criterios.append(crt17)
        criterios.append(crt18)
        criterios.append(crt19)
        criterios.append(crt20)
        criterios.append(crt21)
        criterios.append(crt22)
        criterios.append(crt23)
        criterios.append(crt24)
        criterios.append(crt25)
        
    elif valoracion == 'Motocicleta':
        crt1=ec.Criterio('Documentacion [1-3] [Incluye los documentos que hereda]', Documentacion(), 'rango', 'puntos', 15, [1,3], True)
        crt2=ec.Criterio('Frenos [0] [Desfavorable]', Frenos(),'mayor', None, 0, 0, True) 
        crt3=ec.Criterio('Frenos [1-2] [Nro frenos]', Frenos(),'rango', 'puntos', 15, [1,2], False)
        crt4=ec.Criterio('Carroceria [0-1] [Desfavorable]', Carroceria(), 'mayor', 'puntos', 0, 1, True)
        crt5=ec.Criterio('Carroceria [2]', Carroceria(), 'igual', 'puntos', 5, 2, False)
        crt6=ec.Criterio('Carroceria [3-5]', Carroceria(), 'rango', 'puntos', 15, [3,5], False)
        crt7=ec.Criterio('Iluminacion [0-1] [Desfavorable]', Iluminacion(), 'mayor', 'puntos', 0, 1, True)
        crt8=ec.Criterio('Iluminacion [2]', Iluminacion(), 'igual', 'puntos', 5, 2, False)
        crt9=ec.Criterio('Iluminacion [3-5]', Iluminacion(), 'rango', 'puntos', 15, [3,5], False)
        crt10=ec.Criterio('Suspension [0] [Desfavorable]', Suspension(), 'mayor', 'puntos', 0, 0, True)
        crt11=ec.Criterio('Suspension [1]', Suspension(), 'igual', 'puntos', 5, 1, False)
        crt12=ec.Criterio('Suspension [2]', Suspension(), 'igual', 'puntos', 15, 2, False)
        crt13=ec.Criterio('Emisiones [0] [Bajas]', Emisiones(), 'igual', 'puntos', 15, 0, False)
        crt14=ec.Criterio('Emisiones [1] [Altas]', Emisiones(), 'igual', 'puntos', 5, 1, False)
        crt15=ec.Criterio('Niveles [0-1] [Desfavorable]', Niveles(), 'mayor', 'puntos', 0, 2, True)
        crt16=ec.Criterio('Niveles [2]', Niveles(), 'igual', 'puntos', 5, 2, False)
        crt17=ec.Criterio('Niveles [3-4]', Niveles(), 'rango', 'puntos', 15, [3,4], False)
        crt18=ec.Criterio('Neumaticos [0] [Desfavorable]', Neumaticos(), 'mayor', 'puntos', 0, 0, True)
        crt19=ec.Criterio('Neumaticos [1-2] [Nro neumaticos]', Neumaticos(), 'rango', 'puntos', 15, [1,2], False)
        crt20=ec.Criterio('Motor [0-1] [Desfavorable]', Motor(), 'mayor', 'puntos', 0, 1, True)
        crt21=ec.Criterio('Motor [2-3]', Motor(), 'rango', 'puntos', 15, [2,3], False)
        criterios=ec.Criterios('Criterios de acceso', 55)
       
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
        criterios.append(crt16)
        criterios.append(crt17)
        criterios.append(crt18)
        criterios.append(crt19)
        criterios.append(crt20)
        criterios.append(crt21)
        
    return criterios