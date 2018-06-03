#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: domITV
Descripcion: Fichero de dominio de vehículos de ITV
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 03/06/2018
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
    suspension=ec.Caracteristica(Suspension(),'Correcto')
    emisiones=ec.Caracteristica(Emisiones(),'Bajo')
    niveles=ec.Caracteristica(Niveles(),'Correcto')
    neumaticos=ec.Caracteristica(Neumaticos(),'Correcto')
    motor=ec.Caracteristica(Motor(),'Correcto')
    
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
        ec.Atributo.__init__(self,'Nivel suspension','opciones',None)
class Emisiones(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Nivel emisiones','opciones2',None)
class Niveles(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Niveles marcados','opciones',None)
class Neumaticos(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Estado neumaticos','opciones',None)
class Motor(ec.Atributo):
    def __init__(self):
        ec.Atributo.__init__(self,'Estado motor','opciones',None)

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
        crt14=ec.Criterio('Suspension [Deteriorado][0]: muelles, amortiguadores', Suspension(), 'igual', None, 0, 'Deteriorado', False)
        crt15=ec.Criterio('Suspension [Aceptable][1]', Suspension(), 'igual', None, 5, 'Aceptable', False)
        crt16=ec.Criterio('Suspension [Correcto][2]', Suspension(), 'igual', None, 15, 'Correcto', False)
        crt17=ec.Criterio('Emisiones [Bajo][0]: impurezas bajos', Emisiones(), 'igual', None, 15, 'Bajo', False)
        crt18=ec.Criterio('Emisiones [Alto][1]', Emisiones(), 'igual', None, 5, 'Alto', False)
        crt19=ec.Criterio('Niveles [Deteriorado][0-2]: frenos, aceite, refrigerador, limpiaparabrisas, conductos', Niveles(), 'igual', None, 0, 'Deteriorado', False)
        crt20=ec.Criterio('Niveles [Aceptable][3]', Niveles(), 'igual', None, 5, 'Aceptable', False)
        crt21=ec.Criterio('Niveles [Correcto][4-5]', Niveles(), 'igual', None, 15, 'Correcto', False)
        crt22=ec.Criterio('Neumaticos [Deteriorado][0-2]: estado neumaticos, profundidad dibujo (nro neumaticos)', Neumaticos(), 'igual', None, 0, 'Deteriorado', False)
        crt23=ec.Criterio('Neumaticos [Aceptable][3]', Neumaticos(), 'igual', None, 5, 'Aceptable', False)
        crt24=ec.Criterio('Neumaticos [Correcto][4]', Neumaticos(), 'igual', None, 15, 'Correcto', False)
        crt25=ec.Criterio('Motor [Deteriorado][0-1]: ruido, transmision, fuga de aceite', Motor(), 'igual', None, 0, 'Deteriorado', False)
        crt26=ec.Criterio('Motor [Aceptable][2]', Motor(), 'igual', None, 5, 'Aceptable', False)
        crt27=ec.Criterio('Motor [Correcto][3]', Motor(), 'igual', None, 15, 'Correcto', False)
        criterios=ec.Criterios('Criterios de estado del vehículo', 55)
       
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
        criterios.append(crt26)
        criterios.append(crt27)
        
    elif valoracion == 'Motocicleta':
        crt1=ec.Criterio('Documentacion [1-3]: permiso, tarjeta inspeccion tecnica, comprobante pago seguro', Documentacion(), 'rango', 'puntos', 15, [1,3], True)
        crt2=ec.Criterio('Frenos [Deteriorado][0]: Frenada', Frenos(),'igual', None, 0, 'Deteriorado', False)
        crt3=ec.Criterio('Frenos [Aceptable][1]', Frenos(),'igual', None, 5, 'Aceptable', False) 
        crt4=ec.Criterio('Frenos [Correcto][2]', Frenos(),'igual', None, 15, 'Correcto', False)    
        crt5=ec.Criterio('Iluminacion [Deteriorado][0-1]: largas, cortas, carretera, antiniebla, intermitentes', Iluminacion(), 'igual', None, 0, 'Deteriorado', False)
        crt6=ec.Criterio('Iluminacion [Aceptable][2-3]', Iluminacion(), 'igual', None, 5, 'Aceptable', False)
        crt7=ec.Criterio('Iluminacion [Correcto][4-5]', Iluminacion(), 'igual', None, 15, 'Correcto', False)
        crt8=ec.Criterio('Suspension [Deteriorado][0]: muelles, amortiguadores', Suspension(), 'igual', None, 0, 'Deteriorado', False)
        crt9=ec.Criterio('Suspension [Aceptable][1]', Suspension(), 'igual', None, 5, 'Aceptable', False)
        crt10=ec.Criterio('Suspension [Correcto][2]', Suspension(), 'igual', None, 15, 'Correcto', False)
        crt11=ec.Criterio('Emisiones [Bajo][0]: impurezas bajos', Emisiones(), 'igual', None, 15, 'Bajo', False)
        crt12=ec.Criterio('Emisiones [Alto][1]', Emisiones(), 'igual', None, 5, 'Alto', False)
        crt13=ec.Criterio('Niveles [Deteriorado][0-1]: frenos, aceite, conductos', Niveles(), 'igual', None, 0, 'Deteriorado', False)
        crt14=ec.Criterio('Niveles [Aceptable][2]', Niveles(), 'igual', None, 5, 'Aceptable', False)
        crt15=ec.Criterio('Niveles [Correcto][3]', Niveles(), 'igual', None, 15, 'Correcto', False)
        crt16=ec.Criterio('Neumaticos [Deteriorado][0]: estado neumaticos, profundidad dibujo (nro neumaticos)', Neumaticos(), 'igual', None, 0, 'Deteriorado', False)
        crt17=ec.Criterio('Neumaticos [Aceptable][1]', Neumaticos(), 'igual', None, 5, 'Aceptable', False)
        crt18=ec.Criterio('Neumaticos [Correcto][2]', Neumaticos(), 'igual', None, 15, 'Correcto', False)
        crt19=ec.Criterio('Motor [Deteriorado][0-1]: ruido, transmision, fuga de aceite', Motor(), 'igual', None, 0, 'Deteriorado', False)
        crt20=ec.Criterio('Motor [Aceptable][2]', Motor(), 'igual', None, 5, 'Aceptable', False)
        crt21=ec.Criterio('Motor [Correcto][3]', Motor(), 'igual', None, 15, 'Correcto', False)
        criterios=ec.Criterios('Criterios de estado del vehículo', 55)
       
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