frutas = ['manzana', 'aceituna', 'naranja', 'melon', 'banana']

oracion = ''

cantidad = len(frutas)

for i in range(len(frutas)):
    oracion = oracion + ' ' + frutas[i]
    
    if i == cantidad - 1:
            oracion = oracion + ' and ' + frutas[i]

print(oracion)
