#Imprimiendo con espacios a la izq con %5d (En este caso 5 espacios)
nombre='ejemplo1.txt'
archivo=open(nombre)
i=1
for linea in archivo:
    linea=linea.rstrip('\n')
    print('%5d %s'%(i,linea))
    i+=1
