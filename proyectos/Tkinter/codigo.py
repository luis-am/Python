import tkinter

ventana = tkinter.Tk()

ventana.geometry("400x300")

etiqueta = tkinter.Label(ventana, text = 'Hola mundo', bg = 'red')

# etiqueta.pack()
# Con 'fill' es para estirar.
# etiqueta.pack(fill = tkinter.X)
# etiqueta.pack(fill = tkinter.Y, expand = True)
# etiqueta.pack(fill = tkinter.BOTH, expand = True)

# Con 'side' es para posicionar la etiqueta.
# etiqueta.pack(side= tkinter.BOTTOM)
# etiqueta.pack(side= tkinter.RIGHT)
# etiqueta.pack(side= tkinter.LEFT)

# def saludo():
    # print("Hola")

# Importante: Cada vez que pase una función al botón lo haga sin paréntesis.
# boton1 = tkinter.Button(ventana, text = 'Presiona', padx = 20, pady = 20, command = saludo)
# boton1.pack()

# def saludo(nombre):
    # print("Hola " + nombre)

# Importante: Cada vez que pase una función al botón lo haga sin paréntesis.
# boton1 = tkinter.Button(ventana, text = 'Presiona', padx = 20, pady = 20, command = lambda: saludo('Python'))
# boton1.pack()



# etiqueta = tkinter.Label(ventana)
# etiqueta.pack()

# cajatexto = tkinter.Entry(ventana)
# cajatexto.pack()

# def Imprime():
    # texto = cajatexto.get()
    # print(texto)
    # etiqueta['text'] = texto

# boton1 = tkinter.Button(ventana, text = 'click', command = Imprime)
# boton1.pack()



# boton1 = tkinter.Button(ventana, text = 'boton1')
# boton2 = tkinter.Button(ventana, text = 'boton2')
# boton3 = tkinter.Button(ventana, text = 'boton3')

# boton1.grid(row = 0, column = 0)
# boton2.grid(row = 1, column = 0)
# boton3.grid(row = 5, column = 0)


# ventana.mainloo5()
