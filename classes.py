###### First Video Corey Schafer
# class Empleado:
    # def __init__(self, nombre, apellido, pay):
        # self.nombre = nombre
        # self.apellido = apellido
        # self.pay = pay
        # self.email = nombre + '.' + apellido + '@cibertec.edu.pe'

    # def nombre_completo(self):
        # return 'Mi nombre es {} {}, y tengo {} años de pay. Mi email es {}.'.format(self.nombre, self.apellido, self.pay, self.email)

# empleado_1 = Empleado('Luis', 'Ayala', 28)
# print(empleado_1.email)
# print(empleado_1.nombre)
# print(empleado_1.pay)
# print(empleado_1.apellido)

# empleado_1 = Empleado('Luis', 'Ayala', 28)
# print(empleado_1.nombre_completo())

# empleado_1 = Empleado('Luis', 'Ayala', i)
# print(Empleado.nombre_completo(empleadoi1))









 
 
 

# class Empleado:

    # raise_amount = 100
    # num_empleados = 0

    # def __init__(self, nombre, apellido, pay):
        # self.nombre = nombre
        # self.apellido = apellido
        # self.pay = pay
        # self.email = nombre + '.' + apellido + '@cibertec.edu.pe'
        
        # Empleado.num_empleados += 1

    # def nombre_completo(self):
        # return 'Mi nombre es {} {}, y tengo {} años de pay. Mi email es {}.'.format(self.nombre, self.apellido, self.pay, self.email)
 
    # def apply_raise(self): 
        # self.pay = int(self.pay * Empleado.raise_amount)

# empleado_1 = Empleado('Luis', 'Ayala', 28)
# empleado_2 = Empleado('Soledad', 'Gonzales', 40)
# empleado_3 = Empleado('Jose', 'Ayala', 27)

# print(Empleado.num_empleados)

















# class Empleado:

    # raise_amount = 100
    # num_empleados = 0

    # def __init__(self, nombre, apellido, pay):
        # self.nombre = nombre
        # self.apellido = apellido
        # self.pay = pay
        # self.email = nombre + '.' + apellido + '@cibertec.edu.pe'
        
        # Empleado.num_empleados += 1

    # def nombre_completo(self):
        # return 'Mi nombre es {} {}, y tengo {} años de pay. Mi email es {}.'.format(self.nombre, self.apellido, self.pay, self.email)
 
    # def apply_raise(self): 
        # self.pay = int(self.pay * Empleado.raise_amount)

# empleado_1 = Empleado('Luis', 'Ayala', 28)
# empleado_2 = Empleado('Soledad', 'Gonzales', 40)
# empleado_3 = Empleado('Jose', 'Ayala', 27)

# print(Empleado.num_empleados)


# class Empleados:

    # numero_estudiantes = 0
    # aumento = 2.0

    # def __init__(self, nombre, apellido, pay):
        # self.nombre = nombre
        # self.apellido = apellido
        # self.pay = pay
        # self.email = nombre + '.' + apellido + '@gmail.com' 

        # Empleados.numero_estudiantes += 1

    # def nombre_completo(self):
        # return f'Mi nombre completo es {self.nombre} {self.apellido}, y mi salario es de {self.pay} soles.'

    # def aplicar_aumento(self):
        # self.pay = int(self.pay * Empleados.aumento)

# Creando los objetos
# estudiante_1 = Empleados('Luis', 'Ayala', 1000)
# estudiante_2 = Empleados('Jose', 'Martinez', 2000)
# estudiante_3 = Empleados('Soledad', 'Gonzales', 3000)
# estudiante_4 = Empleados('Alonso', 'Ramirez', 4000)


# Visualizando atributos de objetos
# print(estudiante_1.nombre)
# print(estudiante_1.apellido)
# print(estudiante_1.email)


# Visualizando los metodos de los objetos|
# print(estudiante_1.pay)
# estudiante_1.aplicar_aumento()
# print(estudiante_1.pay)

# print(estudiante_1.__dict__)





# class Employee:
    # def __init__(self, name, )









# class Ropa:
    # def __init__(self):
        # self.marca = 'willow'
        # self.talla = 'M'
        # self.color = 'rojo'
# camisa = Ropa()
# print(camisa.marca)
# print(camisa.talla)
# print(camisa.color)



# class calculadora():
    # def __init__(self, n1, n2):
        # self.suma = n1 + n2
        # self.resta = n1 - n2
        # self.producto = n1 * n2
        # self.division = n1 / n2
# operacion = calculadora(2, 3)
# print(operacion.producto)



# Funciones para atributos

# class Persona:
    # nombre = 'Victor'
    # edad = 27
    # pais = 'Brasil'

# Instanciando el objeto a la clase 'Persona'
# doctor = Persona()

# print('La edad es: ',  doctor.edad)
# print('La edad es: ', getattr(doctor, 'edad'))

# Preguntar si es True or False
# print('El doctor tiene una edad?', hasattr(doctor, 'edad'))

# print('Antes se llamaba: ',doctor.nombre)
# setattr(doctor, 'nombre', 'Hector') # Setear un valor a un atributo
# print('Ahora se llama: ',doctor.nombre)

# delattr(Persona, 'pais') # Se elimina el atributo de una clase
# print(doctor.pais)











# metodo constructor
# class Persona:
    # def __init__(self, nombre, año):
        # self.nombre = nombre
        # self.año = año

    # def descripcion(self):
        # return f'{self.nombre} tiene {self.año} de edad.'

    # def comentario(self, frase):
        # return '{} dice: {}.'.format(self.nombre, frase)

# Creando un objeto
# doctor = Persona('Victor', 26)

# print(doctor.nombre)
# print(doctor.descripcion())
# print(doctor.comentario('El fin justifica los medios.'))














# Modificando un atributo
# class Email:
    # def __init__(self):
        # self.enviado = False

    # def enviar_correo(self):
        # self.enviado = True

# Creando el objeto
# mi_correo = Email()

# print(mi_correo.enviado)
# mi_correo.enviar_correo()
# print(mi_correo.enviado)
















# HERENCIA SINTAXIS

# class NombreSubClase(NombreClaseSuperior):
    # class ClaseBase:
        # Cuerpo de la clase base

    # class DerivadoClase(ClaseBase):
        # Cuerpo de la clase derivada

# HERENCIA EJERCICIO

# class pokemon:
    # pass
    # def __init__(self, nombre, tipo):
        # self.nombre = nombre
        # self.tipo = tipo

    # def descripcion(self):
        # return '{} es un pokemon de tipo: {}.'.format(self.nombre, self.tipo)

# class pikachu(pokemon):
    # def ataque(self, tipoataque):
        # return '{} tiene tipo de ataque: {}'.format(self.nombre, tipoataque)

# class charmander(pokemon):
    # def ataque(self, tipoataque):
        # return '{} tiene tipo de ataque: {}'.format(self.nombre, tipoataque)
    
# nuevo_pokemon = pikachu('boby', 'electrico')
# print(nuevo_pokemon.descripcion())
# print(nuevo_pokemon.ataque('attack trueno'))







# class Pokemon:
    # def __init__(self, nombre, tipo):
        # self.nombre = nombre
        # self.tipo = tipo

    # def descripcion(self):
        # return f'{self.nombre} es un pokemon de tipo {self.tipo}.'

# class pikachu(Pokemon):
    # def ataque(self, tipoataque):
        # return f'{self.nombre} es un Pikachu y tiene tipo de ataque {tipoataque}.'

# class squartle(Pokemon):
    # def ataque(self, tipoataque):
        # return f'{self.nombre} es un Squartle y tiene tipo de ataque {tipoataque}.'

# nuevo_pokemon_1 = pikachu('Richie', 'electrico')
# nuevo_pokemon_2 = squartle('Luca', 'agua')

# print(nuevo_pokemon_1.descripcion())
# print(nuevo_pokemon_2.descripcion())

# print(nuevo_pokemon_1.ataque('Cola de hierro'))
# print(nuevo_pokemon_2.ataque('Hidrobomba'))











# HERENCIA EJEMPLO PRACTICO 2

# class Calculadora:
    # def __init__(self):
        # self.n = numero
        # self.datos = [0 for i in range(numero)]

    # def ingresar_datos(self):
        # self.datos = [int(input('Ingresar datos: '+ str(i+1) + ''))]
