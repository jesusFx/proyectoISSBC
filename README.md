# proyectoISSBC
Trabajo de valoración de la asignatura ISSBC


Correcciones en el software:

	-ckModValoracion:
		-El sistema valora el problema pudiendo tomar en cuenta todos los criterios, y no solo aquellos hasta que se alcanza la puntuación mínima
	-domITV: 
		-Incluye criterios con mayor precisión
		-Corregidos criterios
	-domPan:
		-Incluye criterios con mayor precisión
		-Descartada valoracion única en los criterios, descrita como ''
	-esqConocimiento: 
		-Eliminada la opción múltiple
		-Incluidas dos nuevas opciones (opciones y varios) en la que el primero toma una lista de valores estáticos para ser repetida y el segundo permite incluir valores dinámicos
		-Incluida una opción para indicar en Caracteristica() a qué valoracion se aplican los casos
	-ckVtsValoracion: 
		-La descripcion de criterios devuelta como lista se ha convertido en una tabla de criterios descritos ordenados
		-Ahora al cambiar de valoración también se limpian los cuadros de texto con el resultado y la justificación
		-Se ha corregido la justificacion devuelta
		-Reordenados los apartados gráficos del programa
		-Incluidos en los casos una tercera columna con las valoraciones a las que se aplica los casos debido a la estaticidad de estos