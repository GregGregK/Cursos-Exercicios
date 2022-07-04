#Criar um algoritmo que leia o preço de compra e o preço de venda de 10 mercadorias.
#O algoritmo deverá imprimir quantas mercadorias apresentam:
#•Lucro menor do que 10 %
#•Lucro entre 10% e 20%
#•Lucro > 20%

contador = 1
vPrecoCompra = []
vPrecoVenda = []
vLucro = []

contaMenor10=0
contaEntre10e20=0
contaMaiorQue20=0

while contador <=10:
    precoCompra = float(input("Digite o preço de compra da mercadoria " + str(contador) + ":"))
    precoVenda = float(input("Digite o preço de venda da mercadoria " + str(contador) + ":"))
    lucro = ((precoVenda/precoCompra)-1)*100
    print("Lucro:" + str(lucro) + "%")
    vPrecoCompra.append(precoCompra)
    vPrecoVenda.append(precoVenda)
    vLucro.append(lucro)
    contador+=1

contador=0
while contador<=9:
    if vLucro[contador]<10: contaMenor10+=1
    if vLucro[contador]>=10 and vLucro[contador]<=20: contaEntre10e20+=1
    if vLucro[contador]>20: contaMaiorQue20+=1
    contador+=1

print("Quantidade e Mercadorias com lucro menor do que 10%:" + str(contaMenor10))
print("Quantidade e Mercadorias com lucro entre 10% e 20%:" + str(contaEntre10e20))
print("Quantidade e Mercadorias com lucro maior do que 20%:" + str(contaMaiorQue20))


    
    
