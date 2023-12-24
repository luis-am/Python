birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    nombre = input('Ingresa un nombre: ')
    if nombre == '':
        break

    if nombre in birthdays:
        print('El cumpleaños de tu amigo ' + nombre + ' es ' + birthdays[nombre])
    else:
        print(nombre + ' no se encuentra en la base de datos.')
        rpta = input('Desea agregarlo?: ')
        
        if rpta.lower() in ['si', 'sí', 'yes']:
            nuevo_nombre = input('Ingresa su cumpleaños: ')
            birthdays[nombre] = nuevo_nombre
            print('Base de datos Actualizada: ')
            print(birthdays)
        else:
            print('Get the fuck outta here!')
            break

print(birthdays) 
