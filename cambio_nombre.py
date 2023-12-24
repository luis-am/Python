import os 

# Este es el directorio a modificar de manera recursiva.
directorio = input('Ingresa el directorio a modificar: ')

# Cambiamos al directorio ingresado por el usuario.
os.chdir(directorio) 

# Un loop para recorrer todos los archivos y directorios en el directorio.
for path in os.listdir(directorio):
    # Obtenemos la ruta completa del archivo o directorio
    ruta_completa = os.path.join(directorio, path)
    
    # Verificamos si es un archivo
    if os.path.isfile(ruta_completa):
        # Verificamos si el nombre del archivo contiene '-'
        if '-' in path:
            # Creamos el nuevo nombre reemplazando '-' por '_'
            nuevo_nombre = path.replace('-', '_')
            # Obtenemos la ruta completa del nuevo nombre
            nueva_ruta_completa = os.path.join(directorio, nuevo_nombre)
            # Renombramos el archivo
            os.rename(ruta_completa, nueva_ruta_completa)

print('Nombres de archivos modificados exitosamente.')

