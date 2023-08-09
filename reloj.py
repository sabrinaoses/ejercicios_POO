import datetime # importamos el modulo 
import time # importamos este mod.para parar el prog durante un tiempo
import os # import para limpiar la screem

while True:
    os.system("cls")# vamos a empezar limpiando c/vez que entremos a este True
    dt = datetime.datetime.now() # vamos a crear la hora actual
    print("{}: {}: {}".format(dt.hour,dt.minute,dt.second))
    time.sleep(1)# dormimos el sist 1 second y luego vuelve a entrar al while 