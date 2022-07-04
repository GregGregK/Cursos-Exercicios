#QUESTÃO 2 - GASOLINA/ETANOL (3 PONTOS)

#OBJETIVO: Crie uma função que receba o preço (em reais) por litro da Gasolina e do Etanol e retorne a melhor
#opção. REQUISITOS MÍNIMOS:
#Considere que uma relação de 73% ou menos do preço do etanol em relação ao preço da gasolina, favorece
#o uso do etanol. Se for acima de 73%, é mais viável a utilização da gasolina. Portanto, desenvolva uma
#função que deverá retornar “GASOLINA” ou “ETANOL” de acordo com os argumentos (preços) informados. (2 pontos)
#Desenvolva um algoritmo para realizar o teste da função (conforme exemplo abaixo). (1 pontos)
#EXEMPLO:
#Bem vindo a Calculadora Gasolina/Etanol
#Digite o preço da Gasolina em R$: 3.5
#Digite o preço do Etanol em R$: 2.75
#Para os preços informados, a melhor opção é a utilização da GASOLINA.

# Função
#************************************************
def verificaMelhorCombustivel(pGasolina, pEtanol):
    relacao = pEtanol/pGasolina #Calcula relação entre os combustíveis
    if relacao<=0.73: #verifica se o valor do etanol é 73% o menos do valor da gasolina
        return "ETANOL"
    else:
        return "GASOLINA"

#Entrada de dados (Teste)
#************************************************
print("Bem vindo a Calculadora do melhor combustível!")
valorGasolina = float(input("Digite o preço da Gasolina em R$:"))
if valorGasolina<=0 or valorGasolina>10: #Validação dos dados
    print("Preço inválido!")
    exit()
valorEtanol = float(input("Digite o preço do Etanol em R$:"))
if valorEtanol<=0 or valorEtanol>10:#Validação dos dados
    print("Preço inválido!")
    exit()
melhorCombustivel = verificaMelhorCombustivel(valorGasolina, valorEtanol)
print("Para os preços informados, a melhor opção é a utilização do seguinte combustível:" + melhorCombustivel)


