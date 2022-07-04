#Problema 34:
#Utilizando vetores (para armazenar e ler os dados), elaborar um algoritmo para ler um conjunto de 10 números e informar:
#•Quantos números são iguais a 10.
#•Quantos números são maiores do que a média.
#•Quantos números são iguais a média.

vNumeros = [] #define vetor vNumeros (vazio)
soma = 0
conta10=0
contaMedia=0
contaMaiorMedia=0

for i in range(10):
    vNumeros.append(float(input("Digite o número (" + str(i+1) + " de 10):")))
    soma += vNumeros[i] #soma números
    
media = soma/len(vNumeros) #Calcula média

for i in range(len(vNumeros)):
    if vNumeros[i]==10: conta10+=1
    if vNumeros[i]==media: contaMedia+=1
    if vNumeros[i]>media: contaMaiorMedia+=1

print("Quantidade de números iguais a 10:" + str(conta10))
print("Quantidade de números maiores que a média:" + str(contaMaiorMedia))
print("Quantidade de números iguais a média:" + str(contaMedia))



      

    
               

                         