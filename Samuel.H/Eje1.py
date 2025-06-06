import random
mapa = [[ 0 for fila in range (5)] for col in range(5)]
intentos=0

fila=random.randint(0,4)
col=random.randint(0,4)



mapa[fila][col] = "Tsro" 
for i in range(5):
     
    x = int(input("ingresa la opcion"))
    y = int(input("ingresa la opcion"))
    intentos = intentos +1
    if x == fila and y == col:
        print("el tesoro esta aca")
        mapa[x][y]="T"
        break
    else:
        print("no esta aca")
        mapa[x][y]="X"
    if intentos != mapa:    
        print(f"perdiste,los intentos fueron {intentos} ")
for fila in mapa:
    print(*fila)



        
    
        