def valorRadiano(Graus):
    return (Graus*3.14)/180


def teste():
    graus = float(input("Por favor, o valor em graus:"))
    print("Valor em radianos: " + str(valorRadiano(graus)))
    
teste()