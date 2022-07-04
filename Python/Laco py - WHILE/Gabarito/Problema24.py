contador = 0
acumulador=0

limite = int(input("Digite o limite superior:"))


while contador<limite:
    if contador%2!=0:
        print(contador)
        acumulador = acumulador + contador
    contador+=1
print("Soma:", acumulador)
        
    