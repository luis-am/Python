gatos = []

while True:
    gato = input(f'Ingresa el nombre de un gato ' + str(len(gatos) + 1) + ':')

    if gato == '':
        break

    gatos = gatos + [gato]

print('')
print('Estos son los nombres de tus gatos: ')

for gato in gatos:
    print(gato)
