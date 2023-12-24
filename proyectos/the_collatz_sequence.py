def collatz(number): if number % 2 == 0:
        return number // 2
    else:
        return (3 * number + 1)

while True:
    try:
        number = int(input('Ingresa un numero: '))
    except Exception as e:
        print(f'Recuerda ingresar un valor numérico. Error: {e}\n')
        continue

    print(collatz(number))
    if collatz(number) == 1:
        break

print('Saliste del loop While.')

