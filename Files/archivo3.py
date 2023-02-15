#Quitamos espacio entre lineas con rstrip('\n') usandor ciclo for
nombre='ejemplo1.txt'
archivo=open(nombre)
for linea in archivo:
    linea=linea.rstrip('\n')
    print(linea)
