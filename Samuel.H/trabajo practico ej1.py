estudiantes= [[0 for fila in range(4)]for col in range(3)]


for fila in range(len(estudiantes)):
    for col  in range(len(estudiantes[fila])):
        estudiantes[fila][col] = int(input("ingresa un numero:"))
    
for fila in range(len(estudiantes)):
    print(estudiantes[fila])
fila2=estudiantes[1]
suma=sum(fila2)
print(f"el puntaje total del segundo es:",suma)

