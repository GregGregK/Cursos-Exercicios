#PROBLEMA 41 - NÚMERO PRIMO

#Crie uma função que tem o objetivo de verificar se um número recebido é um número primo. A função deve ser do tipo lógica, isto é, retornar verdadeiro (caso seja primo) ou falso (caso não seja primo).
#Obs.: Os Números Primos são números naturais maiores do que 1 que possuem somente dois divisores, ou seja, são divisíveis por 1 e por ele mesmo.
#Mais informações: https://www.todamateria.com.br/numeros-primos/.

def verificaPrimo(pNumero):
    if pNumero==1: return False
    for i in range(2, pNumero):
        if pNumero%i==0:return False
    return True

numero = int(input("Digite um número:"))
if verificaPrimo(numero)==True:
    print("Número primo")
else:
    print("O número não é primo")

        
    