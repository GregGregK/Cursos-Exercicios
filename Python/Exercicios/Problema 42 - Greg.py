def verificaPrimo(pNumero):
    if pNumero==1: 
        return False
    for i in range(2, pNumero):
        if pNumero %i==0:
            return False
    return True

numero = int(input("Digite até qual número você gostaria de saber a quantidade de números primos:"))
for i in range(2, numero + 1):
    if verificaPrimo(i) == True: print(i)