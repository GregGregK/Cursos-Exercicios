#QUESTÃO 3 - CENSO DEMOGRÁFICO (5 PONTOS)
#OBJETIVO: Desenvolva um algoritmo que receba a informação do estado de origem e do estado civil de uma
#amostra de 8 pessoas residentes na cidade de Florianópolis. Ao final da entrada de dados, o algoritmo deverá
#apresentar as seguintes informações:
#1. Porcentagem de pessoas com origem no estado do Paraná; (1 ponto)
#2. Porcentagem de pessoas com origem no estado de Santa Catarina; (1 ponto)
# 3. Porcentagem de pessoas com origem no estado do Rio Grande do Sul; (1 ponto)
# 4. Quantidade e porcentagem de pessoas solteiras. (1 ponto)
# REQUISITOS MÍNIMOS:
# Os dados obtidos deverão ser armazenados em dois vetores com 8 posições cada;
# O programa permitirá apenas a entrada de dados dos estados da região Sul (PR, SC ou RS); (0,5 ponto)
# O programa permitirá apenas os estados civis “Solteiro(a)” ou “Casado(a)” (S ou C); (0,5 ponto)
# A cada inserção de dados as informações deverão ser obtidas do usuário separadas por ponto e vírgula
# (exemplo abaixo);
# Os dados de saída deverão ser calculados com base nos dados de entrada armazenados nos vetores. Caso
# não sejam utilizados vetores, haverá um desconto de 3 pontos.

vEstado = []
vEstadoCivil = []
contaPR = 0
contaSC = 0
contaRS = 0
contaCasado = 0
contaSolteiro = 0

print("Bem vindo ao Algoritmo de Censo Demográfico:")

for i in range(0,8): # o i irá iterar entre 0 e 7
    entrada = input("Digite o seu estado de origem e seu estado civil separados por “;” (" + str(i+1) + " de 8):")
    
    estado = entrada[0:2].upper() #Primeiras duas posições da string de entrada
    estadoCivil = entrada[-1].upper() #Última duas posições da string de entrada
    
    if estado!= "PR" and estado!="SC" and estado !="RS":
        print("Estado inválido! Programa finalizado.")
        exit()
    
    if estadoCivil != "S" and estadoCivil !="C":
        print("Estado civil inválido! Programa finalizado.")
        exit()
    
    vEstado.append(estado)
    vEstadoCivil.append(estadoCivil)
    
    if vEstado[i] == "PR": contaPR+=1
    elif vEstado[i] == "SC": contaSC+=1
    elif vEstado[i] == "RS": contaRS+=1
    
    if vEstadoCivil[i] == "S": contaSolteiro +=1
    elif vEstadoCivil[i] == "C": contaCasado +=1

pctPR = round((contaPR/8)*100,2) #calcula porcentagem de pessoas no estado do PR
pctSC = round((contaSC/8)*100,2) #calcula porcentagem de pessoas no estado de SC
pctRS = round((contaRS/8)*100,2) #calcula porcentagem de pessoas no estado de RS
pctSolteiro = round((contaSolteiro/8)*100,2) #calcula porcentagem de pessoas solteiras

print("Porcentagem de pessoas com origem no estado do Paraná:" + str(pctPR) + "%")
print("Porcentagem de pessoas com origem no estado do Santa Catarina:" + str(pctSC) + "%")
print("Porcentagem de pessoas com origem no estado do Rio Grande do Sul:" + str(pctRS) + "%")
print("Quantidade e porcentagem de pessoas solteiras:" + str(contaSolteiro) + "(" + str(pctSolteiro) + "%)")


    
        
    
