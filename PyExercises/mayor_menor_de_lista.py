def Pedir_Dato():
    while True:
        try:
            x=int(input('Digite el numero: '))
            break
        except ValueError:
            print('Debe digitar un numero entero!!')
    return x

def Mayor(lista):
    pos_may=0
    for i in range(len(lista)-1):
        if lista[i+1]>lista[pos_may]:
            pos_may=i+1
    return pos_may

def Menor(lista):
    pos_men=0
    for i in range(len(lista)-1):
        if lista[i+1]<lista[pos_men]:
            pos_men=i+1
    return pos_men

def Main():
    print('PROGRAMA PARA DATO MAYOR O MENOR DE LISTA')
    print()
    lista=[]
    n=int(input('Cuantos Datos: '))
    for i in range(n):
        x=Pedir_Dato()
        lista.append(x)
    print(lista)
    pos_may=Mayor(lista)
    pos_men=Menor(lista)
    print('El mayor de la lista es: ',lista[pos_may])
    print('El menor de la lista es: ',lista[pos_men])
Main()
