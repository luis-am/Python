# print(True and True)
# print(True and False)
# print(False and False)
# print(False and True)

# print(True or True)
# print(True or False)
# print(False or False)
# print(False or True)

# print(not True)
# print(not False)


# -----------------------------------------------------------------


# condicionales

# A = int(input('Ingrese un numero: '))
# if A >= 0:
    # print('Es un numero positivo.')
# else:
    # print('Es un numero negativo.')


# Hallar el numero mayor

# A = int(input('Ingresa un primer numero: '))
# B = int(input('Ingresa un segundo numero: '))
# if A > B:
    # print('A es mayor que B.')
# elif A < B:
    # print('B es mayor que A.')
# else:
    # print('Ambos valores son iguales.')


# -----------------------------------------------------------------


# Numero par o impar
# N = int(input('Ingresa un numero: '))
# if N % 2 == 0:
    # print('Este numero es par.')
# else:
    # print('Este numero es impar.')


# -----------------------------------------------------------------


# ELIF
# a = int(input('Ingresa un numero: '))
# if a > 0:
    # R = 'positivo'
# elif a < 0:
    # R = 'negativo'
# else:
    # R = 'neutro'
# print(f'El numero es: {R}')


# -----------------------------------------------------------------


# ELIF CALIFICACION DE NOTAS
# datos
# N: notas
# R: respuesta

# N =float(input('Ingresa un numero: '))
# if N <= 50:
    # R = 'Reprobado'
# elif N <= 80:
    # R = 'Aprobado'
# elif N <= 90:
    # R = 'Sobresaliente'
# else:
    # R = 'Excelente'
# print(f'Su nota es {N}, {R}')


# -----------------------------------------------------------------


# CICLO WHILE
# mostrar la suma de 1 al 6
# mostrar de los n primeros numeros

# N = 5
# N = int(input('Ingresa un numero: '))
# SUMA = 0
# i = 1
# while i <= N:
    # SUMA = SUMA + i
    # i += 1
# print(SUMA)


# -----------------------------------------------------------------


# CICLO WHILE (MULTIPLICACION)

# n = int(input('Ingresa la tabla que deseas ver: '))
# i = 1
# a = 12

# while i <= a:
    # print(f'{n} por {i} es igual a {n*i}')
    # i += 1


# -----------------------------------------------------------------


# Genere los N primeros numeros de forma ascendente

# n = int(input('Ingresa un numero: '))
# i = 0
# while i < n:
    # print(i+1)
    # i += 1

# n = int(input('Ingresa un numero: '))
# i = n
# while i >= 1:
    # print(i)
    # i -=1


# -----------------------------------------------------------------


# CICLO FOR

# for i in 'numero':
    # print(i)

# calcular el numero de vocales en una frase

# frase = str(input('Ingresa una frase: '))
# vocales = 'aeiouAEIOU'
# contador = 0
# for item in frase:
    # if item in vocales:
        # contador += 1
# print(f'El numero de vocales es: {contador}')


# -----------------------------------------------------------------


# sintaxis de rango, ejemplos:
    # range(4) [0,1,2,3]
    # range(2,6) [2,3,4,5]
    # range(3,9,2) [3,5,7]

# tabla de multiplicar

# numero = int(input('Ingresa el numero de la tabla: '))
# for i in range(1,11):
    # print(f'{numero} por {i} es igual a {numero * i}')


# mayor que el anterior

# cantidad = int(input('¿Cuantos valores va ingresar?: '))

# if cantidad < 0:
    # print('Digite un valor positivo.')
# else:
    # primero = int(input('Ingrese un primer numero.'))
    # for i in range(cantidad - 1):
        # numero = int(input('Ingrese un numero mayor que el primero: '))
        # if numero <= primero:
            # print('Este numero es menor que el primero.')
    # print('Gracias por su colaboracion.')


# -----------------------------------------------------------------


# numero = int(input('Ingresa un numero: '))

# for n in range(numero):
    # print(n + 1)
    # n += 1

# for n in range(numero, 0, -1):
    # print(n)
    # n -= 1


# -----------------------------------------------------------------


# la suma de los primeros 'n' numeros:

# numero = int(input('Ingresa un numero: '))
# contador = 0
# for i in range(1, numero + 1):
    # contador = contador + i
# print(f'La suma de los n numeros hasta {numero} es {contador}.')


# -----------------------------------------------------------------


# Numero factorial
# numero = int(input('Ingresa un numero: '))
# total = 1
# for n in range(2, numero +1):
    # total = total * n
# print(total)


# -----------------------------------------------------------------


# FOR LOOPS

# nombres = ['luis', 'soledad', 'jose', 'gustavo', 'john']
# nombres = ('luis', 'soledad', 'jose', 'gustavo', 'john')=
# nombres = {'nombre': 'luis', 'apellido': 'ayala', 'edad': 28}

# personas = [['nombre', 'apellido', 'edad'],
        # ['luis', 'ayala', '28'],
        # ['jose', 'martinez', '26'],
        # ['gustavo', 'caceres', '40'],
        # ['lionel', 'messi', '29'],
        # ['cristiano', 'ronaldo', '54'],
        # ['gerard', 'pique', '11'],
        # ['andre', 'iniesta', '45']
        # ]

# mayores_de_30 = []

# for persona in personas[1:]:
    # edad = persona[2]
    # edad = int(edad)
    # persona[2] = edad

    # if edad >= 30:
        # mayores_de_30.append(persona)

# for i in mayores_de_30:
    # print(i)


# -----------------------------------------------------------------


# gente = [
        # ['luis', 'ayala', '28'],
        # ['christina', 'ramirez', '30'],
        # ['kilian', 'mbappe', '11'],
        # ['cristiano', 'ronaldo', '53'],
        # ['lionel', 'messi', '65']
        # ]

# for persona in gente:
    # if persona[0] == 'kilian':
        # break
    # print(persona)


# -----------------------------------------------------------------


# languages = [['Spanish', 'English',  'French', 'German'], ['Python', 'Java', 'Javascript', 'C++']]

# for x in languages:
    # print("------")
    # for lang in x:
        # print(lang)


# nombre del archivo que desea leer
nombre_archivo = input('Ingresa el nombre del archivo: ')
longitud = []

try:
    with open(nombre_archivo, "r") as file:
        for row in file:
            longitud.append(row.strip())
            
        for i in longitud:
            print(i)

except FileNotFoundError:
    print(f'El archivo {nombre_archivo} no fue encontrado.')


# -----------------------------------------------------------------


# Funcion strip
# cadena = '   Hola mundo!      '
# cadena_limpia = cadena.strip()
# print(cadena_limpia)
# cadena =  '__________Hola mundo!________'
# cadena_limpia = cadena.strip('_')
# print(cadena_limpia)
