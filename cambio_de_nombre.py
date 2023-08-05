# Script para cambiar todos aquellos nombres de folderes que tengan espacios en guion bajo.

import os

directorio = input('Ingresa la ruta a modificar: ')
os.chdir(directorio)      # Cambiando al directorio en donde se realizará el cambio de nombre
folders = os.listdir() # listando los folderes      # Listando los files dentro del directorio cambiado

for carpeta in folders:                             # Por cada carpeta en la lista folder
    if ' ' in carpeta:                              # Si dentro de cada carpeta hay un espacio ' '
        nueva_carpeta = carpeta.replace(' ', '_')   # Reemplaza ese espacio por un guion bajo, y lo pasamos a una nueva variable
        os.rename(carpeta, nueva_carpeta)           # Renombra la carpeta con el nuevo nombre.

print(folders)                                      # Lista todos los files dentro del folder
