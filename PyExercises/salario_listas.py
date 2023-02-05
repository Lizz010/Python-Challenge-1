N=int(input("Digite la cantidad de empleados: "))
nombres=[]
salarios=[]

for x in range(N):
    nombres.append(input("Digite el nombre del empleado: "))
    salarios.append(int(input("Digite el salario del empleado: ")))
for x in range(N-1,-1,-1):
    print(nombres[x])
    print(salarios[x])

    

    
    
