frutas={1:1.35,2:0.8,3:0.85,4:0.7}
print("Digite el código de una fruta teniendo en cuenta:")
print("*************************************************")
print("|1.PLATANO                                      |")
print("|2.MANZANA                                      |")
print("|3.PERA                                         |")
print("|4.NARANJA                                      |")
print("*************************************************")
codigo=int(input())
kilos=float(input("Digite la cantidad de kilos: "))
pagar=0
if (codigo in frutas):
    pagar=kilos * frutas[codigo]
else:
    print("La fruta no existe")
print("El valor a pagar es: " +  "${:,.1f}".format(pagar))

    

