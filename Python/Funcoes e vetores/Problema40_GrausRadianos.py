#PROBLEMA 40 - CONVERSÃO GRAUS-RADIANOS
#Criar uma função que converta valores em graus para radianos. Após isso, desenvolva um algoritmo para o teste dessa função.

def valorRadianos(vGraus):
    return (vGraus*3.14)/180


def teste():
    g = float(input("Por favor, o valor em graus:"))
    print("Valor em radianos: " + str(valorRadianos(g)))
    
teste()