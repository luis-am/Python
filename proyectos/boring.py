NUMERO_SECRETO = 15
NUMERO_INTENTOS = 5

def obtener_numero():
    try:
        return int(input('Ingresa un numero: '))
    except Exception as e:
        print(f'Ingresa un valor numérico. 🖕')
        return obtener_numero()


for i in range(1, NUMERO_INTENTOS + 1):

    numero_user = obtener_numero()

    if numero_user < NUMERO_SECRETO:
        print('Numero muy bajo.')
        
    elif numero_user > NUMERO_SECRETO:
        print('Numero muy alto.')

    else:
        print(f'Muy bien, acertaste en el intento {i}.')

else:
    print('No acertaste ninguno lamentablemente.')
