contador = 1
limite = int(input("Digite o limite superior:"))
soma = 0
texto = ""
while contador < limite:
    if contador%2!=0:
        soma = soma + contador
        texto = texto + str(contador) + " "
    contador = contador + 2
print(texto)
print("Soma:" , soma)
    