#print(RETO 3)
#print('TIENDA TU VECINO')

codp=[]
nomp=[]
cantc=[]
vuni=[]
tpiva=[]

vprod=[]
viva=[]
vfin=[]

n = int(input('Cantidad de Productos: '))
for i in range(n):
    cp=int(input('Codigo del Producto: '))
    codp.append(cp)
    np=str(input('Nombre del Producto: '))
    nomp.append(np)
    cc=float(input('Cantidad Comprada: '))
    cantc.append(cc)
    vu=float(input('Valor Unitario: '))
    vuni.append(vu)
    tiva=int(input('Tipo de Iva <1-2-3>: '))
    tpiva.append(tiva)

    vprod.append(cc*vu)
    
    if tiva == 1:
        iva=0
        viva.append(iva)
        vfin.append((cc*vu)+iva)
    elif tiva == 2:
        iva =(cc*vu)*0.05
        viva.append(iva)
        vfin.append((cc*vu)+iva)
    elif tiva == 3:
        iva =(cc*vu)*0.19
        viva.append(iva)
        vfin.append((cc*vu)+iva)

print(len(codp))
print(len(nomp))
print(len(cantc))
print(len(vuni))
print(len(tpiva))
for i in range(n):
    print(codp[i])
    print(nomp[i])
    print(vprod[i])
    print(vfin[i])
    
print(sum(vfin))
print(sum(viva))
