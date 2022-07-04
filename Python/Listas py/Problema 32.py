#PROBLEMA 32 - PAR OU ÍMPAR
#Armazenar 15 números inteiros em um vetor vNumeros e imprimir uma listagem numerada
#contendo o número e uma das mensagens: par ou impar.

vNumeros = []
contador = 1

#Entrada de Dados
while contador <= 15:
    numero = int(input("Digite um número inteiro " + str(contador) + " de 15:"))
    vNumeros.append(numero)
    contador +=1

#Saida de dados
print("*************************************************")
i = 0
while i < len(vNumeros):
    if vNumeros[i]%2==0:
        print(str(vNumeros[i]) + ": Par")
    else:
        print(str(vNumeros[i]) + ": Ímpar")
    i+=1