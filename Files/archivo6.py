#Apertura de archivos
#archivo=open(nombre,'tipo')
#'r' read abre el archivo para lectura
#'w' write abre el archivo para escritura
#'a' append abre el archivo para agregar contenido

#Abriendo archivo para lectura con 'r'
nombre='ejemplo1.txt'
archivo=open(nombre,'r')
i=1
for linea in archivo:
    linea=linea.rstrip('\n')
    print('%d %s'%(i,linea))
    i+=1
