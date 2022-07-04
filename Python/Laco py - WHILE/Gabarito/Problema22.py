'''Escreva um algoritmo de um programa que o usuário possa entrar com 10 números.
 A medida que o usuário digita cada um dos números , o programa deve exibir o número e o quadrado.
'''

contador = 1
numero = 0

while contador<=10:
    contador = contador + 1
    numero = float(input("Digite um número:"))
    nQuadrado = numero * numero
    print("Quadrado de{} : {}".format(numero, nQuadrado))
    

