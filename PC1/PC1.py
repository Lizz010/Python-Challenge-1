#print('RETO 1')
#print('TIENDA TU VECINO')

print('Codigo del producto: ')
cd=int(input())
print('Nombre del producto: ')
np=str(input())
print('Cantidad comprada: ')
cc=float(input())
print('Valor Unitario: ')
vu=float(input())

vp = cc*vu
vi = vp*0.19
vfin = vp+vi

print('Codigo de Producto: ',cd)
print('Nombre del Producto: ',np)
print('Valor del Producto: ',vp)
print('Valor final del Producto: ',vfin)
