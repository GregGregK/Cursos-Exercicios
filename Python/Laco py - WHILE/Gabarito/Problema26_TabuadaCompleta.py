#entrada de dados (pergunta)
resposta = input("Deseja visualizar a tabuada completa?")

#inicializa variáveis
contador1 = 1
contador2 = 1
resultado = 0

if resposta.upper() == "S": #Se resposta for 's' ou 'S'
    while contador1 <=10: 
        while contador2<=10:
            resultado  = contador1 * contador2 #calcula multiplicação
            texto = "{0:02}".format(contador1) + " x " + "{0:02}".format(contador2) + " = " + str(resultado) #monta texto de saída
            print(texto) #exibe texto de saída
            contador2+=1 #incrementa contador2
        contador2 = 1 #volta contador2 para 1
        contador1 +=1 #incrementa contador1
        
        