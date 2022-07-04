#PROBLEMA 41 - NÚMERO PRIMO (SEQUÊNCIA)

#Crie a lógica para um programa que gera uma sequência de número primos entre 1 e um valor definido pelo usuário. Para isso,
#utilize a função que verifica se o número é primo (do problema 41).
#Digite o valor máximo da sequência de números primos: 100
#Sequência de número até 100:
#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,79, 83, 89, 97

def verificaPrimo(pNumero):
    if pNumero==1: return False
    for i in range(2, pNumero):
        if pNumero%i==0:return False
    return True

numero = int(input("Digite o valor máximo da sequência de números primos:"))
for i in range(2, numero + 1):
    if verificaPrimo(i) == True: print(i)
        
    