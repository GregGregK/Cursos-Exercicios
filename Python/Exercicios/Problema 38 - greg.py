PI = 3.14
def calculoArea(raio):
    return PI*(raio**2) 
def calculoPerimetro(raio):
    return (2*PI*raio)
def testar():
    r = float(input("Digite o raio da circunferência:"))
    area = calculoArea(r)
    perimetro = calculoPerimetro(r)
    print("Área:", str((area)))
    print("Perímetro:", str((perimetro)))

testar()