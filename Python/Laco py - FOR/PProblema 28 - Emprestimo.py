#PROBLEMA 28 - EMPRÉSTIMO BANCÁRIO
#Suponha que o “Banco Nacional da Família” faz empréstimos a juros
#zero para os clientes de baixa renda (renda familiar menor ou igual a
#um salário mínimo). Desenvolva um algoritmo de um programa que
#obtenha o nome do cliente, a renda familiar e o valor do
#empréstimo. Após isso, o programa deve mostrar o saldo estimado
#para cada mês pelos próximos 10 meses. Assuma que não há
#cobrança de juros nessa conta, que o cliente não faça novos
#empréstimos e que o cliente salde sua dívida em pagamentos
#mensais de 10% do valor original. Caso a renda familiar seja superior
#a um salário mínimo, o programa deve informar que não é possível
#realizar o empréstimo.

salario_minimo = 1212
contador = 0

print("Bem vindo ao Banco Nacional da Família!")

nome = input("Por favor, digite seu nome:")
salario = float(input("Digite o valor da sua renda Familiar:"))

if salario > salario_minimo:
    print("Renda familiar superio a 1 salário mínimo. Infelizmente, não será possível realizar o empréstimo.")
    exit()

emprestimo = float(input("Por favor, digite o valor que deseja emprestar:"))
saldo = emprestimo

while contador < 10:
    contador +=  1
    saldo = saldo - (emprestimo * 0.1)
    if contador == 10 and saldo<1: saldo=0
    print("Saldo no mês " + str(contador) + ":" + str(round(saldo,2)))