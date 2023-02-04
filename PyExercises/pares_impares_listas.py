numeros=[]
pares=[]
impares=[]
dato=int(input("Digite un número: "))
while (dato!=-1):
    numeros.append(dato)
    dato=int(input("Digite un número: "))
for x in numeros:
    if (x%2==0):
        pares.append(x)
    else:
        impares.append(x)
print("Lista Original.")
print(numeros)
print("Lista Pares.")
print(pares)
print("Lista Impares.")
print(impares)   
