
def area_triangulo (b,a):
    return (b*a)/2


#Ahora creamos el programa principal
base=float(input("Digite la base: "))
altura=float(input("Digite la altura: "))
area= area_triangulo(base,altura)
print("El área es: " +  str(area))

