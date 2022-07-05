def calMulta(velocidade,limite):
    if velocidade >= limite*1.20:
        return"o valor da multa é 130,16"
    elif velocidade < limite * 1.20 and velocidade >= limite * 1.50:
        print(f'Sua velocidade de {velocidade} o limite da via era {limite} e a multa era {calculo}')
    elif velocidade <= limite:
        return"Velocidade é igual ao limite = 0"
    else:
        print(f'Sua velocidade de {velocidade} o limite da via era {limite} e a multa era {calculo}')
    
velocidade = float(input('Digite sua velocidade mo quirido: '))
limite = float(input('Digite o limite da rua: '))
calculo = calMulta(velocidade,limite)
print(calculo)

