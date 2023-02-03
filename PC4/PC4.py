#print(RETO 4)
#print('TIENDA TU VECINO')

codp=[]
nomp=[]
cantc=[]
vuni=[]
tpiva=[]
vprod=[]
viva=[]
vfin=[]

n = int(input('Cantidad de Productos Comprados: '))
for i in range(n):
    cp=int(input('Codigo Producto: '))
    codp.append(cp)
    np=(input('Nombre Producto: '))
    nomp.append(np)
    cc=float(input('Cantidad Comprada: '))
    cantc.append(cc)
    vu=float(input('Valor Unitario: '))
    vuni.append(vu)
    tiva=int(input('Tipo Iva <1-2-3>: '))
    tpiva.append(tiva)

    vprod.append(cantc[i]*vuni[i])

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

def ordenamiento():
    for i in range(1,n):
        for j in range(n-i):
            if nomp[j]>nomp[j+1]:
                codp[j], codp[j+1] = codp[j+1], codp[j]
                nomp[j], nomp[j+1] = nomp[j+1], nomp[j]
                cantc[j], cantc[j+1] = cantc[j+1], cantc[j]
                vuni[j], vuni[j+1] = vuni[j+1], vuni[j]
                tpiva[j], tpiva[j+1] = tpiva[j+1], tpiva[j]

                vprod[j], vprod[j+1] = vprod[j+1], vprod[j]
                viva[j], viva[j+1] = viva[j+1], viva[j]
                vfin[j], vfin[j+1] = vfin[j+1], vfin[j]
ordenamiento()
for i in range(n):
    print('Codigo: ',codp[i])
    print('Nombre: ',nomp[i])
    print('Valor iva: ',viva[i])
    print('Valor producto: ',vprod[i])
    print('Valor final: ',vfin[i])
vf=sum((vfin))
vi=sum((viva))
print('Valores finales: ',vf)
print('Valores iva: ',vi)
