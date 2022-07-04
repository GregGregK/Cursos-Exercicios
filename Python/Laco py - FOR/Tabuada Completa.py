#entrada de dados (pergunta)
resposta = input("Deseja visualizar a tabuada completa?")

#inicializa variáveis
resultado = 0
if resposta.upper() == "S": #Se resposta for 's' ou 'S'
    for i in range(1,11): 
        for j in range(1,11):
            resultado  = i * j #calcula multiplicação
            texto = "{0:02}".format(i) + " x " + "{0:02}".format(j) + " = " + str(resultado) #monta texto de saída
            print(texto) #exibe texto de saída
        