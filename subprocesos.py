
import subprocess
import os

# subprocess.run('ls', shell=True) # En windows
# subprocess.run(['ls', '-la'])
# subprocess.run(['ip', 'add'])

# p1 = subprocess.run(['ls', '-la'])
# p1 = subprocess.run(['ls', '-la'], capture_output=True)
# p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)

# print(p1.args)
# print(p1.returncode)
# print(p1.stdout)
# print(p1.stdout.decode())
# print(p1.stdout)


# with open('output.txt', 'w') as f:
    # p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)

# p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True)
# p1 = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL)

# print(p1.returncode)
# print(p1.stderr)

# p1 = subprocess.run(['cat', 'output.txt'], capture_output=True, text=True)
# p2 = subprocess.run(['grep', '-n', 'try'], capture_output=True, text=True, input=p1.stdout)
# print(p2.stdout)









# a = subprocess.Popen('dir', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
# print(a.stdout.read())

# a = open(os.devnull, 'w')

# p = subprocess.call(['ping', '10.0.0.30', '-c', '3'], stdout=a, stderr=subprocess.STDOUT)

# if p == 0:
    # print('El comando se ejecuto correctamente.')
# else:
    # print('Fallo la ejecucion del comando.')
