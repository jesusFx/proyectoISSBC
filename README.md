# Proyecto Sistema Basado en Conocimiento [Valoraci�n]

Descripci�n: Dise�o de un sistema basado en conocimiento orientado a valoraci�n, para la asignatura de Ingenier�a Software de Sistemas Basados en Conocimiento de la Universidad de C�rdoba (Curso 2017-2018)

Entorno de dise�o: 

	Eclipse Oxigen (versi�n de abril 2018)
	
Lenguajes usados en el proyecto: 
	
	Python 2.7.14
	PyDev 6.4.1 para Eclipse
	PyQT 4.11.4 para Python 2.7 (instalador externo)
		- Puede encontrarse en el siguiente enlace: https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/
	
�ltimas correcciones en el software:

	-ckModValoracion:
		-El sistema valora el problema pudiendo tomar en cuenta todos los criterios, y no solo aquellos hasta que se alcanza la puntuaci�n m�nima
	-domITV: 
		-Incluye criterios con mayor precisi�n
		-Corregidos criterios
	-domPan:
		-Incluye criterios con mayor precisi�n
		-Descartada valoracion �nica en los criterios, descrita como ''
	-esqConocimiento: 
		-Eliminada la opci�n m�ltiple
		-Incluidas dos nuevas opciones (opciones y varios) en la que el primero toma una lista de valores est�ticos para ser repetida y el segundo permite incluir valores din�micos
		-Incluida una opci�n para indicar en Caracteristica() a qu� valoracion se aplican los casos
	-ckVtsValoracion: 
		-La descripcion de criterios devuelta como lista se ha convertido en una tabla de criterios descritos ordenados
		-Ahora al cambiar de valoraci�n tambi�n se limpian los cuadros de texto con el resultado y la justificaci�n
		-Se ha corregido la justificacion devuelta
		-Reordenados los apartados gr�ficos del programa
		-Incluidos en los casos una tercera columna con las valoraciones a las que se aplica los casos debido a la estaticidad de estos
		
Estado del proyecto:

	Verificado que el ejecutable no presenta errores de ning�n tipo