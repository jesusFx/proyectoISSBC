#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre: ckModValoracion
Descripcion: Funciones del sistema
Asignatura: ISSBC
Autor: Jesus Jimenez Roman
Fecha: 05/06/2018
"""

import domPan, domITV
import esqConocimiento as ec

def devolverDominio():
    '''Devolvemos el dominio de conocimiento elegido'''
    dom = None
    if ec.dominioActual == 'ITV':
        dom = domITV
    elif ec.dominioActual == 'Pan comun':
        dom = domPan
    return dom

class Tarea():
    '''Definimos la tarea a realizar'''
    def __init__(self):
        self.objetivo = u'Valoración'
        self.descripcion = u'Valora y decide sobre un conjunto de criterios'

class Metodo():
    def __init__(self):
        self.descripcion = u'Método de resolución de problemas'

class Inferencia():
    def __init__(self):
        pass
    def execute(self):
        pass


'''Recibe un caso que se valorará a partir de los criterios establecidos'''
class MetodoValoracion(Metodo):
    def __init__(self, caso):
        self.caso = caso
        self.criterios = None
        self.resultados = None
        self.pmaxima = 0
        self.pnecesario = 60
        self.decision = None #decision que va a gobernar el bucle
        self.explicacion = u"PROCEDIMIENTO \n\n"
        self.dom = devolverDominio()

    def execute(self):
        dom = devolverDominio() #Almacenamos el dominio
        
        print "\nEjecutando tarea de valoración..." 
        self.explicacion += u"Ejecutando tarea de valoración...\n"
        
        self.decision = dom.ec.Decision(0, " ") #Inicializamos la variable decision (0-continua, -1-para, 1-Acepta)
        self.resultados = dom.ec.Resultados() #Inicializamos la variable Resultado

        print "\nEspecificando criterios.."
        self.explicacion += u"\nEspecificando criterios...\n"
        
        self.criterios = Especificar(self.caso).execute() #Almacenamos los criterios de cada base de conocimiento
        self.pmaxima = self.criterios.puntuacionmax() #La suma del valor de todos los criterios
        self.pnecesario = self.criterios.pnecesario #Puntos necesarios para cada caso
        
        self.ncriterios = self.criterios.ncriterios 
        
        #Mientras que no se decida nada...
        while(self.decision.decision == 0):
            #Selecciona un criterio
            self.selector = Seleccionar(self.criterios)
            self.criterio = self.selector.execute()
            
            #Si la lista no esta vacia, eliminamos un criterio
            #Si no hay mas criterios, salimos del bucle y equiparamos antes
            if(self.criterio == None):
                print "\nNo quedan mas criterios...finalizando..." #Mostramos en consola
                self.explicacion += u"\nNo quedan mas criterios\nFinalizando...\n"
                self.decision, self.valexpl = Equiparar(self.resultados, self.pmaxima, self.pnecesario, True,self.ncriterios).execute()
                self.explicacion += self.valexpl
                break
            else:
                self.selector.pop()
                
            print "\nCriterio seleccionado: " + self.criterio.nombre
            self.explicacion += u"\nCriterio seleccionado: " + self.criterio.nombre + '\n\n'
            
            #Se evalua el caso con un criterio
            self.valor, self.valexpl = Evaluar(self.caso, self.criterio).execute()
            self.explicacion += self.valexpl
            
            #Añade el nuevo valor a los resultados
            self.resultados.append(self.valor)
            
            #Se equipara el resultado
            self.decision, self.valexpl = Equiparar(self.resultados, self.pmaxima, self.pnecesario, False,self.ncriterios).execute()
            self.explicacion += self.valexpl
            
            self.ncriterios -= 1
            
        print u'\nTarea finalizada'
        self.explicacion += u"Tarea finalizada\n"
        #Se anade la justificacion al objeto decision
        self.decision.addexp(self.explicacion)
        #devuelve la decision
        return self.decision



#Recibe un caso y devuelve los criterios,
#cosa que no tiene sentido, pero se hace asi para respetar
#el modelo de valoracion de la teoria
class Especificar(Inferencia):
    def __init__(self, caso):
        Inferencia.__init__(self)
        self.caso = caso
    def execute(self):
        dom = devolverDominio()
        valoracion = dom.valoracionActual
        print valoracion
        self.criterios = dom.criterios(valoracion)
        return self.criterios


#Recibe unos criterios y devuelve uno solo
class Seleccionar(Inferencia):
    def __init__(self,criterios):
        Inferencia.__init__(self)
        self.criterios = criterios
    def pop(self):
        if len(self.criterios.lcriterios) > 0:
            self.criterios.lcriterios.pop(0)
    def execute(self):
        if len(self.criterios.lcriterios) > 0:
            return self.criterios.lcriterios[0]
        else:
            return None


#Recibe un objeto Caso y un objeto Criterio y devuelve un objeto Valor con una puntuacion
class Evaluar(Inferencia):
    def __init__(self, caso, criterio):
        Inferencia.__init__(self)
        self.criterio = criterio
        self.caso = caso
        self.valor = None
        self.explicacion = " "

    def execute(self):
        dom = devolverDominio()
        print "\nEvaluando criterio..."
        self.explicacion += u"\tEvaluando criterio seleccionado...\n\t=========================="
        self.explicacion += u"\n\tTipo de comparación: " + self.criterio.tipoComparacion
        self.explicacion += u"\n\tValor necesario: " + str(self.criterio.valor)
        self.explicacion += u"\n\tPuntuación: " + str(self.criterio.puntuacion)
        self.explicacion += u"\n\tTerminal: " + str(self.criterio.terminal)
        #Se recorre cada caracteristica del caso y se va comparando con el criterio
        for carac in self.caso.caracteristicas:
            if carac.atributo.nombre == self.criterio.atributo.nombre:
                #Si un valor es terminal y falla, se manda un valor negativo, indicando que no hace falta seguir
                #Si no es terminal y falla, se manda 0, no dandose puntos
                #Si no falla, se manda la puntuacion del criterio
                #Se repite esto con cada tipo de comparacion por lo que se genera un objeto valor por cada atributo del caso
                if self.criterio.tipoComparacion == 'rango':
                    self.explicacion += u"\n\n\t-->Característica:\n\t    " + carac.atributo.nombre
                    self.explicacion += u"\n\t    Valor: " + str(carac.valor)
                    if carac.valor < self.criterio.valor[0] or carac.valor > self.criterio.valor[1]:
                        if self.criterio.terminal == True:
                            self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" no se encuentra en el rango " + str(self.criterio.valor) + u"\n"
                            self.explicacion += u"\n\t    Puntuación " + str(-1) + u" puntos, fuera de rango válido"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, -1)
                        else:
                            self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" no se encuentra en el rango " + str(self.criterio.valor) + u"\n"
                            self.explicacion += u"\n\t    Puntuación +0 puntos\n"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, 0)
                    else:
                        self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" pertenece al rango " + str(self.criterio.valor) + u"\n\n"
                        self.explicacion += u"\n\t    Puntuación +" + str(self.criterio.puntuacion) + u" puntos\n"
                        self.valor = dom.ec.Valor(self.criterio, self.caso, self.criterio.puntuacion)


                elif self.criterio.tipoComparacion == 'igual':
                    self.explicacion += u"\n\n\t-->Característica:\n\t    " + carac.atributo.nombre
                    self.explicacion += u"\n\t    Valor: " + str(carac.valor)
                    if carac.valor != self.criterio.valor:
                        if self.criterio.terminal == True:
                            self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" no es igual a " + str(self.criterio.valor) + u"\n"
                            self.explicacion += u"\n\t    Puntuación " + str(-1) + u" puntos, no es valor válido"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, -1)
                        else:
                            self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" no es igual a " + str(self.criterio.valor) + u"\n"
                            self.explicacion += u"\n\t    Puntuación +0 puntos\n"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, 0)
                    else:
                        self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" es igual a " + str(self.criterio.valor) + u"\n\n"
                        self.explicacion += u"\n\t    Puntuación +" + str(self.criterio.puntuacion) + u" puntos\n"
                        self.valor = dom.ec.Valor(self.criterio, self.caso, self.criterio.puntuacion)
                        
                elif self.criterio.tipoComparacion == 'distinto':
                    self.explicacion += u"\n\n\t-->Característica:\n\t    " + carac.atributo.nombre
                    self.explicacion += u"\n\t    Valor: " + str(carac.valor)
                    if carac.valor == self.criterio.valor:
                        if self.criterio.terminal == True:
                            self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" es igual a " + str(self.criterio.valor) + u"\n"
                            self.explicacion += u"\n\t    Puntuación " + str(-1) + u" puntos, no es valor válido"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, -1)
                        else:
                            self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" es igual a " + str(self.criterio.valor) + u"\n"
                            self.explicacion += u"\n\t    Puntuación +0 puntos\n"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, 0)
                    else:
                        self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" no es igual a " + str(self.criterio.valor) + u"\n\n"
                        self.explicacion += u"\n\t    Puntuación +" + str(self.criterio.puntuacion) + u" puntos\n"
                        self.valor = dom.ec.Valor(self.criterio, self.caso, self.criterio.puntuacion)


                elif self.criterio.tipoComparacion == 'mayor':
                    self.explicacion += u"\n\n\t-->Característica:\n\t    " + carac.atributo.nombre
                    self.explicacion += u"\n\t    Valor: " + str(carac.valor)
                    if carac.valor < self.criterio.valor:
                        if self.criterio.terminal == True:
                            self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" no es mayor que " + str(self.criterio.valor) + u"\n"
                            self.explicacion += u"\n\t    Puntuación " + str(-1) + u" puntos, no es mayor que el valor indicado"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, -1)
                        else:
                            self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" no es mayor que " + str(self.criterio.valor) + u"\n"
                            self.explicacion += u"\n\t    Puntuación +0 puntos"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, 0)
                    else:
                        self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" es mayor que " + str(self.criterio.valor) + u"\n\n"
                        self.explicacion += u"\n\t    Puntuación +" + str(self.criterio.puntuacion) + u" puntos"
                        self.valor = dom.ec.Valor(self.criterio, self.caso, self.criterio.puntuacion)


                elif self.criterio.tipoComparacion == 'menor':
                    self.explicacion += u"\n\n\t-->Característica:\n\t    " + carac.atributo.nombre
                    self.explicacion += u"\n\t    Valor: " + str(carac.valor)
                    if carac.valor > self.criterio.valor:
                        if self.criterio.terminal == True:
                            self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" no es menor que " + str(self.criterio.valor) + u"\n"
                            self.explicacion += u"\n\t    Puntuación " + str(-1) + u" puntos, no es menor que el valor indicado"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, -1)
                        else:
                            self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" no es menor que " + str(self.criterio.valor) + u"\n"
                            self.explicacion += u"\n\t    Puntuación +0 puntos"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, 0)
                    else:
                        self.explicacion += u"\n\t    El valor " + str(carac.valor) + u" es menor que " + str(self.criterio.valor) + u"\n\n"
                        self.explicacion += u"\n\t    Puntuación +" + str(self.criterio.puntuacion) + u" puntos"
                        self.valor = dom.ec.Valor(self.criterio, self.caso, self.criterio.puntuacion)
                elif self.criterio.tipoComparacion == 'categorica':
                    self.explicacion += u"\n\n\t-->Característica:\n\t    " + carac.atributo.nombre
                    self.explicacion += u"\n\t    Valor: " + str(carac.valor)
                    encontrado = False
                    for i in self.criterio.valor:
                        if i == carac.valor:
                            encontrado = True
                    if encontrado == False:
                        self.explicacion += u"\n\t    El valor "+ str(carac.valor) + u" no se encuentra dentro de "+ str(self.criterio.valor) + u"\n"
                        if self.criterio.terminal == True:
                            self.explicacion += u"\n\t    Puntuación " + str(-1) + u" puntos, no está contenido en la categoría"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, -1)
                        else:
                            self.explicacion += u"\n\t    Puntuación +0 puntos"
                            self.valor = dom.ec.Valor(self.criterio, self.caso, 0)
                    else:
                        self.explicacion += u"\n\t    El valor "+ str(carac.valor) + u" se encuentra dentro de "+ str(self.criterio.valor)+ u"\n\n"
                        self.explicacion += u"\n\t    Puntuación +" + str(self.criterio.puntuacion) + u" puntos"
                        self.valor = dom.ec.Valor(self.criterio, self.caso, self.criterio.puntuacion)

                        
        return (self.valor, self.explicacion)

#Recibe un objeto Resultados, que es una lista de objetos Valores
#y devuelve un objeto Decision, que contendra la decision para el caso
#la variable de entrada final especifica si es el ultimo criterio a evaluar,
#asi, si no se ha llegado a la puntuacion minima y es el ultimo, se rechaza
class Equiparar(Inferencia):
    def __init__(self, resultados, puntuacionmax, pnecesario, final,ncriterios):
        Inferencia.__init__(self)
        self.resultados = resultados
        self.puntuacion = resultados.show()
        self.puntuacionmax = puntuacionmax
        self.pnecesario = pnecesario
        self.final = final
        self.explicacion = u" "
        self.ncriterios = ncriterios
        
    def execute(self):
        dom = devolverDominio()
        print "\nEquiparando..."
        self.explicacion += u"\n\n\n\tEquiparando el caso \n\t=========================="
        #por cada valor, si encontramos un negativo, se termina y se rechaza,
        #si no, se acumulan los valores.
        for valor in self.resultados.lresultados:
            if(valor.puntuacion == -1):
                print "\nRECHAZADO"
                self.explicacion += u"\n\tValor terminal -> DESFAVORABLE VALOR NO VÁLIDO\n\n\n"
                return (dom.ec.Decision(-1,"caso rechazado"), self.explicacion)
        #una vez tiene los valores, si la puntuacion es mayor que el  minimo
        #se acepta y no se sigue el algoritmo, si este es el ultimo y la puntuacion
        #no es suficiente, se rechaza y acaba, si no se llega al minimo pero
        #quedan mas criterios, se continua
        if(self.puntuacion * 100 / self.puntuacionmax > self.pnecesario and self.ncriterios <= 0):
            print "\nACEPTADO" 
            self.explicacion += u"\n\tPuntuación suficiente (" + str(self.puntuacion) + u") -> FAVORABLE\n\n\n"
            return (dom.ec.Decision(1, "caso aceptado"), self.explicacion)
        elif(self.final == True):
            print "\nRECHAZADO"
            self.explicacion += u"\n\tPuntuación insuficiente (" + str(self.puntuacion) + u") -> DESFAVORABLE\n\n\n"
            return (dom.ec.Decision(-1, "finalizado insuficiente"), self.explicacion)
        else:
            print "\nCONTINUAR EVALUANDO..."
            self.explicacion += u"\n\tPuntuación insuficiente (" + str(self.puntuacion) + u") -> Continuar evaluando\n\n\n"
            return (dom.ec.Decision(0, "continuar evaluando"), self.explicacion)