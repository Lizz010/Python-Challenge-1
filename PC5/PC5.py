#print(RETO 5)
#print('TIENDA TU VECINO')

#Listas
codp=[]
cantc=[]
tpiva=[]
vprod=[]
viva=[]
vfin=[]

#Diccionario de articulos
productos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}

#Ingreso de datos / Recorriendo datos con ciclo for
n= int(input('Cantidad de Productos Comprados: '))
for i in range(n):
    cp=int(input('Codigo Producto <1-2-3-4-5-6-7-8>: '))
    codp.append(cp)
    cc=float(input('Cantidad Comprada: '))
    cantc.append(cc)
    tiva=int(input('Tipo Iva <1-2-3>: '))
    tpiva.append(tiva)
    print()
#Operacion para obtener 'vprod[]'
    vprod.append(cantc[i]*precios.get(codp[i]))
#Operaciones segun tipo de iva para definir iva=viva[],vfin[]
    if tiva == 1:
        iva=0
        viva.append(iva)
        vfin.append((cc*precios.get(codp[i])+iva))
    elif tiva == 2:
        iva=(cc*precios.get(codp[i]))*0.05
        viva.append(iva)
        vfin.append((cc*precios.get(codp[i])+iva))
    elif tiva == 3:
        iva=(cc*precios.get(codp[i]))*0.19
        viva.append(iva)
        vfin.append((cc*precios.get(codp[i])+iva))

#Metodo Ordenamiento()
def OrdenamientoDatos():
    for i in range(1,n):
        for j in range(n-i):
            if codp[j]>codp[j+1]:
                codp[j], codp[j+1] = codp[j+1], codp[j]
                cantc[j], cantc[j+1] = cantc[j+1], cantc[j]
                tpiva[j], tpiva[j+1] = tpiva[j+1], tpiva[j]
                vprod[j], vprod[j+1] = vprod[j+1], vprod[j]
                viva[j], viva[j+1] = viva[j+1], viva[j]
                vfin[j], vfin[j+1] = vfin[j+1], vfin[j]
#Llamando funcion "OrdenamientoDatos()"
OrdenamientoDatos()

#Imprimiendo datos / Recorriendo datos con ciclo for
print('FACTURA DE COMPRA:')
for i in range(n):
    print('Codigo: ',codp[i])
    print('Nombre: ',productos.get(codp[i]))
    print('Valor Producto: ',vprod[i])
    print('Valor final: ',vfin[i])
    print()
vf=sum((vfin))
vi=sum((viva))
print()
print('Valores Total Compra: ',vf)
print('Valores Total iva: ',vi)
 
