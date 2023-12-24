import random

lista_general = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z', ',', ';', '.', ':', '-', '_', '+', '*', '{', '}', '[', ']', '~', '^', '!', '"', '#', '$', '%', '&', '/', '(', ')', '\'', '?', '@', '=', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

lista_simbolos = [',', ';', '.', ':', '-', '_', '+', '*', '{', '}', '[', ']', '~', '^', '!', '"', '#', '$', '%', '&', '/', '(', ')', '\'', '?', '@', '=']

# lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, ' ']
# lista_numeros = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

##### Funciones


### Generacion de números:

def generar_numeros(repeticion):
    resultado = ""
    for _ in range(repeticion):
        for _ in range(len(lista_numeros)):
            item = random.choice(lista_numeros)
            resultado = resultado + str(item)
    return resultado


### Generacion de letras:

def generar_letras(repeticion):
    resultado = ""
    for _ in range(repeticion):
        for _ in range(len(lista_letras)):
            item = random.choice(lista_letras)
            resultado = resultado + item
    return resultado


### Generacion de simbolos:

def generar_simbolos(repeticion):
    resultado = ""
    for _ in range(repeticion):
        for _ in range(len(lista_simbolos)):
            item = random.choice(lista_simbolos)
            resultado = resultado + item
    return resultado


### Generacion de general:

def generar_general(repeticion):
    resultado = ""
    for _ in range(repeticion):
        for _ in range(len(lista_general)):
            item = random.choice(lista_general)
            resultado = resultado + item
    return resultado


def main():
    while True:
        try:
            solicitud = input('Ingresa una letra ["n", "l", "g" "s"]: ')
            repeticion = int(input('Ingresa el número de repeticiones: ' ))
        except Exception as e:
            print('Ingresa un valor válido.')
            continue

        if solicitud not in ['n', 'l', 'g', 's']:
            break
        elif solicitud == 'n':
            resultado = generar_numeros(repeticion)
        elif solicitud == 'l':
            resultado = generar_letras(repeticion)
        elif solicitud == 's':
            resultado = generar_simbolos(repeticion)
        elif solicitud == 'g':
            resultado = generar_general(repeticion)

        return resultado

resultado_total = main()
print(resultado_total)
