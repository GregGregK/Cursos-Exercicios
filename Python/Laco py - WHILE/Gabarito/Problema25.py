#EXERCÍCIO 25 - TABUADA
#Criar um algoritmo em Python exiba a tabuada de um número informado pelo usuário (entre 1 e 10).

tabuada = int(input("Digite um valor entre 1 e 10:"))
contador =1
texto = ""
resultado = 0

while contador<=10:
    resultado = tabuada * contador
    texto = texto + str(tabuada) + " X " + str(contador) + " = " + str(resultado) + "\n"
    contador+=1

print("Tabuada do", str(tabuada) + ":")
print(texto)
    