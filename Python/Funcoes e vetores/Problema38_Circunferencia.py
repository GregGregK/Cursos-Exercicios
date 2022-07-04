#PROBLEMA 38 - CIRCUNFERÊNCIA
#Escreva um algoritmo para um programa que calcule a área e o perímetro de uma circunferência (em metros).
#Para isso o usuário deverá inserir o valor do raio (em metros).
#O programa deverá realizar os cálculos por meio das funções calcula_area e calcula_perimetro (com base unicamente no valor do raio).

PI = 3.14
def calcula_area(raio):
    return PI*(raio**2) #área pi*r²

def calcula_perimetro(raio):
    return (2*PI*raio)

def teste():
    r = float(input("Por favor digite o raio da circunferência (em metros):"))
    area = calcula_area(r)
    perimetro = calcula_perimetro(r)
    print("Área:", str(round(area,2)))
    print("Perímetro:", str(round(perimetro,2)))

teste()

    

