#PROBLEMA 35 - temp MÉDIA
#Criar um algoritmo que receba a temp média de cada mês do ano, em centigrados, e armazene essas temps em um vetor.
#Além disso, imprimir as temps de todos os meses, a maior e a menor temp do ano e em que mês aconteceram.

vMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
vTempMes = []
maiorTemp = 0
menorTemp = 0
mesMenorTemp = 0
mesMaiorTemp = 0

for i in range(12):
    tempMes = float(input("Digite a temp média do mês de " + vMeses[i] + " (em °C):"))
    vTempMes.append(tempMes)
    if i ==0:
        maiorTemp = tempMes
        menorTemp = tempMes
    
    if tempMes > maiorTemp:
        maiorTemp = tempMes
        mesMaiorTemp = i
        
    if tempMes < menorTemp:
        menorTemp = tempMes
        mesMenorTemp = i
print('********************* SAÍDA DE DADOS *****************************')

for i in range(len(vTempMes)):
    print("Temperatura média no mês de " + vMeses[i] + ":" + str(vTempMes[i]) + "°C")
    
print("Maior temperatura: " + str(maiorTemp) + "°C no mês de " + vMeses[mesMaiorTemp] + ".")
print("Menor temperatura: " + str(menorTemp) + "°C no mês de " + vMeses[mesMenorTemp] + ".")

    
    
        
    
                
                             
    



