#Creacion de archivo para guardar datos en una lista
Datos=['Primera linea','Segunda linea','Tercera linea','Cuarta linea']
nombre='lista.txt'
archivo=open(nombre,'w')
for linea in Datos:
    archivo.write(linea)
    archivo.write('\n')
archivo.close()

Texto=[] #Lista 'Texto'
archivo=open(nombre,'r') #Abriendo archivo
linea=archivo.readlines() #Agregando lo de archivo a var linea
Texto.append(linea) #Agregando a lista 'Texto' contenido de var linea
print(Texto) #Imprimiendo lista 'Texto'
archivo.close() #Cerrando Archivo
