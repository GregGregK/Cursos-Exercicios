valor = int(input("Digite um número inteiro:"))

#inicializa variáveis
contador = valor - 1
resultado = valor
saida = str(valor) + "!" + " = " + str(valor)

#print(saida)

while contador>=1:
    resultado = resultado * contador #realiza multiplicação (considerando resultado anterior)
    saida = saida + " x " + str(contador) #monta saída de dados
    print(saida) #mostra saída intermediária (não é obrigatório)
    contador = contador - 1 #decremento do contador

saida = saida + " = " + str(resultado)
print(saida)
    
               