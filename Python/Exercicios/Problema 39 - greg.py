def calcularVelocidadeMedia(distancia, tempo):
    tempoHoras = tempo/60
    velocidadeMedia = round(distancia/tempoHoras,2)
    return str(velocidadeMedia) + "km/h"

def teste():
    d = float(input("Digite a distância percorrida:"))
    t = float(input("Digite o tempo decorrido:"))
    print("Velocidade média: " + calcularVelocidadeMedia(d,t))
    
teste()