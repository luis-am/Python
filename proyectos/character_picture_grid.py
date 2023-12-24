grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

num_filas = len(grid)
num_columnas = len(grid[0])

# Recorrer cada columna y luego cada fila, imprimiendo el carácter correspondiente
# for columna in range(num_columnas):
    # for fila in range(num_filas):
        # print(grid[fila][columna], end='')
    # print()
print(num_columnas)
