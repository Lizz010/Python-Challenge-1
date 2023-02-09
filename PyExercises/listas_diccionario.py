N=int(input("Digite la cantidad: "))
lista=[]
resultado={}
for w in range(N):
    lista.append(int(input("Digite un número ")))
print(lista)
for tierra in lista:
    resultado.setdefault(tierra,lista.count(tierra))
print(resultado)
