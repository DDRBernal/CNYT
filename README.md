# CALCULADORA NUMEROS COMPLEJOS, VECTORES Y MATRICES

Esta calculadora nos permite hacer distintas operaciones con numeros complejos. Los numeros complejos
son una extensión de los números reales y forman un cuerpo algebraicamente cerrado. Se representan con
una parte real y una imaginaria expresada con la letra i.
Ej:
 3+2i donde 2i es la parte imaginaria y 3 es la parte real.

Para la calculadora lo vamos a representar de esta forma:
 (3,2) 

# INSTALANDO PYTHON

Vamos a instalar primero python (recomendable la version 3.7 para Windows) de la siguiente pagina
https://www.python.org/downloads/, una vez instalado podemos verificar en cmd si esta instalado y que
version.

Con el atajo Windows + R podemos acceder rápidamente, nos abrirá una pequeña pantalla donde escribir, aquí  escribiremos cmd.

![window](https://user-images.githubusercontent.com/46855679/64225937-16432100-cea3-11e9-9d21-b5403dfe4fd1.JPG)

.

![cmd](https://user-images.githubusercontent.com/46855679/64483407-e196d880-d1c6-11e9-9030-645e59b41312.JPG)

Ahora para verificar que tenemos python en nuestro ordenador, escribimos "py" (sin comillas).

![py](https://user-images.githubusercontent.com/46855679/64225594-9f595880-cea1-11e9-8311-b047bb101c01.JPG)

Ahora procederemos a descargar los archivos, luego tendremos los siguientes archivos.

![arPY](https://user-images.githubusercontent.com/46855679/64482602-9aa2e600-d1ba-11e9-914a-0c681f5b7abb.JPG)

El que vamos a utilizar es el archivo cnyt_Calculadora.py dando click derecho en el, y luego "Edit whit IDLE" como lo
podemos observar.

![idle](https://user-images.githubusercontent.com/46855679/64482604-9f679a00-d1ba-11e9-86bd-570a11bd3c47.JPG)

Ahora nos abrira el codigo y para poder probarlo solo falta presionar la tecla F5. Ahora nos mostrara los metodos
que podemos usar, cabe resaltar que para poder usarlos debemos tener en cuenta que:

   1) Para colocar numeros complejos (parte real e imaginaria), lo ponemos entre parentesis (1,2) (que seria 1+2i)
   2) Para utilizar una funcion, la escribimos seguido de parentesis donde ira nuestros numeros o vectores o matrices 
   3) Para los vectores de numeros reales o complejos utilizamos corchetes "[]", ej: [2,3,(1,2)]
   4) Para las matrices lo asumimos como vector de vectores, ej: [[2,3,(1,2)],[1,(3,4),1]]
   
Un ejemplo:

![prueba](https://user-images.githubusercontent.com/46855679/64482699-94ae0480-d1bc-11e9-9855-87da7e00e5fd.JPG)

   
# ¿QUE FUNCIONES OFRECE ESTE PROGRAMA?

Tiene 2 partes, una de operaciones de numeros complejos (o reales) y otra de vectores, matrices complejas.

# FUNCIONES NUMEROS COMPLEJOS

Para los numeros complejos se ofrecen:

	1) suma de 2 numeros complejos, la funcion es sumaC(numero1,numero2)
	2) resta de 2 numeros complejos, la funcion es restaC(numero1,numero2)
	3) multiplicacion de 2 numeros complejos, la funcion es multiplicacionC(numero1,numero2)
	3) division de 2 numeros complejos, la funcion es divisionC(numero1,numero2)
	4) el modulo de un numero complejo, la funcion es moduloC(numero)
	5) el conjugado de un numero complejo, la funcion es comjugadoC(numero)
	6) el polar de un numero complejo, la funcion es polarC(numero)
	7) el cartesiano de un numero complejo, la funcion es complejoC(numero)
	8) la fase de un numero complejo, la funcion es faseC(numero)
	
# FUNCIONES VECTORES Y MATRICES COMPLEJAS

Para los vectores y matrices se ofrecen:

	1) multiplicacion de un vector con un escalar, llamada multiplicacionEscalar(vector,c)
	2) suma de vectores, llamada sumaV(vectorA,vectorB)
    3) inversa de un vector, llamado inversaV(vector)
	4) suma de matrices, llamado sumaM(matrizA,matrizB)
	5) resta de matrices, llamado restaM(matrizA,matrizB)
	6) multiplicacion de matrices, llamado multiplicacionM(matrizA,matrizB) 
	7) multiplicacion de una matriz con un vector, llamado multiplicacionMV(matriz,vector)
	8) inversa de una matriz, llamado inversaM(matriz)
	9) multiplicacion de una matriz con un numero entero (escalar), llamado multiplicacionME(matriz,c)
	10) transpuesta de una matriz, llamado transpuestaM(matriz)
	11) conjugado de una matriz, llamado conjugadaM(matriz)
	12) adjunta de una matriz, llamado adjuntaM(matriz)
	13) distancia entre 2 matrices, llamado distanciaM(matrizA,matrizB)
	14) norma de una matriz, llamado normaM(matriz)
	15) verificar si una matriz es hermitian o no, llamado checkHermitian(matriz)
	16) verificar si una matriz es unitaria o no, llamado checkUnitaria(matriz)
	17) producto tensor de 2 matrices, llamado productoTensor(matrizA,matrizB)
	18) realizar una accion de una matriz sobre un vector, llamado accionM(matriz,vector)
	
	
# PRUEBAS UNITTEST

Las pruebas con ayuda de una libreria de python llamado unittest nos permite verificar el comportamiento de 
varias funciones, para asi poder rectificar su comportamiento en el programa.

![test](https://user-images.githubusercontent.com/46855679/64483567-dbeec200-d1c9-11e9-92c9-fb510a7d2fa6.JPG)


# REALIZAR LAS PRUEBAS UNITTEST

Para esto nos dirijimos a la carpeta que contenga los archivos descargados, una vez ahí en la direccion escribimos cmd
y presionamos enter.

![carpeta](https://user-images.githubusercontent.com/46855679/64491282-5d773c00-d22c-11e9-9faa-7667da16035d.JPG)

Cuando se halla abierto la consola escribiremos lo siguiente:

![test1](https://user-images.githubusercontent.com/46855679/64491327-20f81000-d22d-11e9-8e88-26309127684a.JPG)

Automaticamente se habran realizado las pruebas.

# AUTOR

**DAVID RICARDO OTÁLORA BERNAL**






