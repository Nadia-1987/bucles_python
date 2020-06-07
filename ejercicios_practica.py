

#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuante cuantes números ingresados hay y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''
    sumatoria = 0
    cantidad_numeros = 0
    
    inicio = int (input('Ingrese el primer numero de la secuencia:\n'))
    fin = int (input('Ingrese el ultimo numero de la secuencia\n'))
     
    for numero in range(inicio,fin):
        sumatoria += numero
        cantidad_numeros += 1
            
    print('la suma de los numeros es:',sumatoria, 'y la cantidad de numeros es:',cantidad_numeros)


    


   
    # promedio = sumatoria / cantidad_numeros
    promedio = sumatoria / cantidad_numeros
    # Imprimir resultado en pantalla
    print('El promedio es:',promedio)

def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''

    numero_1 = 10
    numero_2 = 20
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multiplicacion = numero_1 * numero_2
    division = numero_1 / numero_2
    exponente = numero_1 ** numero_2
    
    while True:

        operador = str(input('Ingrese el simbolo de la operacion que desee operar:\n'))
        if operador == 'FIN':
            break
        elif operador == '+':
            print('el resultado de la suma entre',numero_1,'y',numero_2,'es',suma)
        elif operador == '-':
            print('el resultado de la resta entre',numero_1,'y',numero_2,'es',resta)
        elif operador == '*':
            print('el resultado de la multiplicacion entre',numero_1,'y',numero_2,'es',multiplicacion)
        elif operador == '/':
            print('el resultado de la division entre',numero_1,'y',numero_2,'es',division)
        elif operador == '**':
            print('el resultado del exponente de',numero_1,'a',numero_2,'es',exponente) 
        else:
            print('error')
    






def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''
    
    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0 
    cantidad_ausentes = 0
    cantidad_notas = 0
              


    
       # Aquí debe contar cuantos ausentes hubo

    for nota in notas:
        if nota < 0:
            cantidad_ausentes += 1
        elif nota >= 0:
            cantidad_notas +=1
            sumatoria += nota 
   
    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas
    promedio = sumatoria / cantidad_notas

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado


    if promedio >= 90:
        print('A')
    else:
        if promedio >= 80:
            print('B')
        else:
            if promedio >= 70:
                    print('C')
            else:
                    if promedio >= 60:
                            print('D') 
                    else:
                            if promedio < 60:     
                                print('F')

    # Imprima en pantalla al cantidad de ausentes
    print('La cantidad de ausentes es:',cantidad_ausentes)


def ej4():
    print("Mi primer pasito en data analytics")

    '''
    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo   
    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados
    
    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted
    '''
     
    
    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_len = 0

    for temperatura in temp_dataloger:
        if (temperatura_max is None) or (temperatura > temperatura_max):
            temperatura_max = temperatura
            temperatura_sumatoria += temperatura
    print('la temperatura maxima es:',temperatura_max)

    for temperatura in temp_dataloger:
        if (temperatura_min is None) or (temperatura < temperatura_min):
            temperatura_min = temperatura   
            temperatura_sumatoria += temperatura
    print('la temperatura minima es:',temperatura_min)
               
        
    
       

        
    temperatura_len = len(temp_dataloger)

        
    temperatura_promedio = temperatura_sumatoria / temperatura_len

    print('la temperatura maxima es', temperatura_max)
    print(max(temp_dataloger))

    print('la temperatura minima es',temperatura_min)
    print(min(temp_dataloger))

    print('el promedio de las temperaturas es',temperatura_promedio)    

   


    # Colocar el bucle aqui......

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo

    if (temperatura_min >= 19) and (temperatura_max <= 28):
        print('nos encontramos en verano')
    else:
        if (temperatura_min >= 11) and (temperatura_max <= 24):
            print('nos encontramos en otoño')
        else:
            if (temperatura_min >= 8) and (temperatura_max <= 14):
                print('nos encontramos en invierno')
            else:
                if (temperatura_min >= 10) and (temperatura_max <= 24):
                    print('nos encontramos en primavera')


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''
    consulta_orden = int(input('Ingrese 1 para ordenar alfabeticamente, 2 por longitud de palabra, 3 para terminar)\n'))
    lista = []
    palabras_deseadas = 0
    
    while consulta_orden == 3:
        print('termino el programa por haber ingresado 3')
        break        
    
    while consulta_orden == 1:
        palabras_deseadas = str(input('ingrese una palabra:\n'))
        lista.append(palabras_deseadas) 
        palabras_deseadas = str(input('ingrese otra palabra:\n'))
        lista.append(palabras_deseadas)
    
    for palabra in palabras_deseadas:
        


        


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
