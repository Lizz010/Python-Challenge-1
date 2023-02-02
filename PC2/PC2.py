#print('RETO 2')
#print('TIENDA TU VECINO')
n = int(input('Cantidad de Productos: '))
totVen = 0
totIva = 0
for i in range(n):
    print('Codigo del Producto: ')
    codp=int(input())
    print('Nombre del Producto: ')
    np=input()
    print('Cantidad comprada del Producto: ')
    cp=float(input())
    print('Valor Unitario: ')
    vu=float(input())
    print('Tipo de Iva <1-2-3>: ')
    tiva=int(input())
    
    vp=cp*vu

    if tiva == 1:
        iva=0
    elif tiva == 2:
        iva = vp*0.05
    elif tiva == 3:
        iva = vp*0.19
    
    vfin=vp+iva

    totVen = totVen + vfin
    totIva = totIva + iva

    print('Codigo del Producto: ',codp)
    print('Nombre del Producto: ',np)
    print('Valor del Producto: ',vp)
    print('Valor final del Producto: ',vfin)
    print()
    
print('Total de Ventas: ',totVen)
print('Total Iva: ',totIva)
