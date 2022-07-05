def funcDobro(num):
    var = num * 2
    return var

def funcQuadrado(num):
    var = num * num
    return var

soma = 0
for i in range(3):
    num = int(input('Digite um número: '+ str(i+1)+':'))
    soma += num
    quadrado = funcQuadrado(soma)
    dobro = funcDobro(soma)
print(soma)
print('Quadrado: ', quadrado)
print('Dobro:', dobro)

numeros = []
for i in range(3):
    num = int(input('Digite seu numero'))
    numeros.append(num)
    quadradoNumeros= funcQuadrado(num) 
    dobroNumeros= funcDobro(num)
    print(quadradoNumeros)
    print(dobroNumeros)
print(numeros, quadradoNumeros, dobroNumeros)