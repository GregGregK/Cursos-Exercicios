#PROBLEMA 39 - VELOCIDADE MÉDIA

#Criar uma função que calcule a velocidade média do veículo (em km/h).
#A função deverá receber como argumentos a distância percorrida (em km) e o tempo de viagem (em minutos).
#Após isso, desenvolva um algoritmo para o teste dessa função.

def calculaVMedia(distancia, tempo):
    #velocidade média = d/t
    #d: distância em km
    #t: tempo em horas
    tHoras = tempo/60
    vMedia = round(distancia/tHoras,2)
    return str(vMedia) + " km/h"

def teste():
    d = float(input("Por favor, digite a distância percorrida (em km):"))
    t = float(input("Por favor, digite o tempo decorrido (em minutos):"))
    print("Velocidade média: " + calculaVMedia(d,t))
    
teste()

    


