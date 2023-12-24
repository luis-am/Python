while True:
    x = input('Ingresa un número para contar hasta: ')
    if x == "quit" or x == "q":
        break
        
    x = int(x)
    y = 1

    while True:
        print(y)
        y+=1
        if y>x:
            break
