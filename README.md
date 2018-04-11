# Series de campeonatos de futbol

Se realiza el sorteo entre 8 equipos de la competencia. Las selecciones se encuentran numeradas del 1 al 32, las mejores han sido pre asignadas como “cabeza de serie”; una por cada grupo y no se sorteará su ubicación en la serie

Las selecciones restantes se sortearán la ubicación en cada serie (grupo) para completar los cuatro participantes por serie.
grupo 	1 	2 	3 	4 	5 	6 	7 	8
cabeza [grupo] 	3 	7 	9 	12 	22 	25 	26 	30

Sorteo de serie (luego de copiar los cabezas de grupo)
selección 	1 	2 	3 	4 	5 	6 	7 	8 	9 	… 	32
serie [selección] 	0 	0 	1 	0 	0 	0 	2 	0 	3 	0 	0

El algoritmo solicita cuáles son los 8 equipos que serán cabezas de serie, asigne aleatoriamente (y sin repeticiones) los 24 equipos restantes, al final muestre el listado de las series resultantes.
