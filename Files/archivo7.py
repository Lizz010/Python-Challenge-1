#Apertura de archivos
#archivo=open(nombre,'tipo')
#'r' read abre el archivo para lectura
#'w' write abre el archivo para escritura
#'a' append abre el archivo para agregar contenido

#Creando archivo para escritura con 'w'
nombre='ejemplo2.txt'
archivo=open(nombre,'w')
archivo.write('Este es el segundo ejemplo\n')
archivo.write('De escritura de archivos\n')
archivo.write('En lenguaje Python.\n')
archivo.close()
#Adicionando informacion a archivo
archivo=open(nombre,'a')
archivo.write('Esta en una nueva linea \n')
archivo.write('Para el archivo anterior')
archivo.close()
#Lectura e impresion de archivo con 'r'
nombre='ejemplo2.txt'
archivo=open(nombre,'r')
for linea in archivo:
    linea=linea.rstrip('\n')
    print(linea)
archivo.close()
