# try:
    # f = open('/home/luisam/folderprueba/file10')
# except Exception:
    # print('Sorry, eres estupido.')
    
try:
    f = open('/home/luisam/folderprueba/file10')
    # var = bad_var
except FileNotFoundError as a:
    print(a)
except NameError as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
   print('Ejecutando finalmene...') 


# try:
    # pass
# except Exception:
    # pass
# else:
    # pass
# finally:
    # pass


