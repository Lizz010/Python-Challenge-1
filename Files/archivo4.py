#Quitamos espacio entre lineas con rstrip('\n') usando ciclo while
nombre='ejemplo1.txt'
archivo=open(nombre)
linea=archivo.readline()
while linea!='':
    linea=linea.rstrip('\n')
    print(linea)
    linea=archivo.readline()
