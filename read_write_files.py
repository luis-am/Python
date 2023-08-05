# File objects

# f = open('/home/luisam/folderprueba/file1', 'r') # 'r' es read, 'w' es write, 'r+' es read and write
# print(f.name)
# print(f.mode)
# print(f.closed)
# f.close()

# with open('/home/luisam/folderprueba/file1', 'r') as f:
    # f_contents = f.read()
    # f_contents = f.readlines()
    # f_contents = f.readline()
    # print(f_contents, end='')

    # for line in f:
        # print(line, end='')

    # f_contents = f.read(100)            # Lee los 100 primeros caracteres del file.
    # print(f_contents, end='')


    # zise_to_read = 10
    # f_contents = f.read(zise_to_read)
    # while len(f_contents) > 0:
        # print(f_contents, end='*')
        # f_contents = f.read(zise_to_read)
    # print(f_contents)
    

    # tamaño_lectura = 10
    # contenido = f.read(tamaño_lectura)
    # while len(contenido) > 0:
        # print(contenido, end='-')
        # contenido = f.read(tamaño_lectura)

    
    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='*')
    # f.seek(0) # empieza desde el primer caracter
    # f_contents = f.read(size_to_read)
    # print(f_contents)


# with open('/home/luisam/folderprueba/file2', 'w') as f:
    # f.write('Test')
    # f.seek(0)
    # f.write('R')

# with open('/home/luisam/folderprueba/file1', 'r') as rf:
    # with open('/home/luisam/folderprueba/file1_copy', 'w') as wf:
        # for line in rf:
            # wf.write(line)
