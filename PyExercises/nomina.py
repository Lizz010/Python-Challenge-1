def ordenar (N,codigo,horas,aporte,salario_final):
    for x in range(N-1):
        for y in range(x+1,N):
            if (codigo[y]<codigo[x]):
                temp=codigo[x]
                codigo[x]=codigo[y]
                codigo[y]=temp
                temp=horas[x]
                horas[x]=horas[y]
                horas[y]=temp
                temp=aporte[x]
                aporte[x]=aporte[y]
                aporte[y]=temp
                temp=salario_final[x]
                salario_final[x]=salario_final[y]
                salario_final[y]=temp
    return codigo,horas,aporte,salario_final
    

empleados={1:"Carlos", 2:"María",3:"Sandra",4:"Carolina",5:"Omar",6:"Juan",7:"Sarai",8:"Diana"}
salarios= {1:8500,2:3000,3:2000,4:6000,5:95000,6:3600,7:7000,8:7300}
codigo=[]
horas=[]
aporte=[]
salario_final=[]
valor_nomina=0
total_aporte=0
cantidad_horas=0

N=int(input("Digite la cantidad de empleados: "))
for x in range(N):
    codigo.append(int(input("Digite el código: ")))
    horas.append(int(input("Digite la cantidad de horas: ")))
    aporte.append(int(input("Digite el aporte: ")))
    

for x in range(N):
    salario_mes=salarios[codigo[x]]
    hora_normal=salario_mes/240
    valor_hora_adicional=hora_normal * 1.25
    salario_final.append(salario_mes + (valor_hora_adicional * horas[x]) - aporte[x])
    valor_nomina+= salario_final[x]
    total_aporte+=aporte[x]
    cantidad_horas+=horas[x]

codigo,horas,aporte,salario_final= ordenar(N,codigo,horas,aporte,salario_final)

#Imprimir
for x in range(N):
    print(codigo[x])
    print(empleados.get(codigo[x]))
    print(salario_final[x])
print(valor_nomina)
print(total_aporte)
print(cantidad_horas)

    
    

    


