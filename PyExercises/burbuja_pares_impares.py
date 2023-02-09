numeros=[]
pares=[]
impares=[]
for w in range(10):
    numeros.append(int(input("Digite un número: ")))
print(numeros)
for x in numeros:
    if (x%2==0):
        pares.append(x)
    else:
        impares.append(x)

print(pares)
print(impares)
#Ordenamos la lista PAR ascendentemente
for x in range(len(pares)-1):
    for y in range(x+1,len(pares)):
        if (pares[y]<pares[x]):
            temp=pares[x]
            pares[x]=pares[y]
            pares[y]=temp
print(pares)

#Ordenamos la lista IMPAR descendentemente
for x in range(len(impares)-1):
    for y in range(x+1,len(impares)):
        if (impares[y]>impares[x]):
            temp=impares[x]
            impares[x]=impares[y]
            impares[y]=temp
print(impares)
