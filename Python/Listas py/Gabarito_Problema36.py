#PROBLEMA 36 - REORDENA VETOR

#Criar uma algoritmo que leia os elementos de um vetor com 10 posições e escreva-o.
#Em seguida, troque o primeiro elemento pelo último, o segundo pelo penúltimo, o terceiro pelo antepenúltimo, a assim sucessivamente.
#Mostre o vetor depois das trocas.

vValores = []
for i in range(10):
    vValores.append(int(input("Digite um valor:")))
print(vValores)

k = 9

for j in range(int(len(vValores)/2)):
    temp = vValores[j]
    vValores[j] = vValores[k]
    vValores[k] = temp
    k-=1

print(vValores)