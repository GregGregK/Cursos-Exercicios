print('Ola cliente')
preco = float(input("Digite o preço de custo do produto: "))
comissao = float(input("Digite o numero da porcentagem da comissão do vendedor: "))
desconto = float(input("Digite o numero da porcentagem de desconto do cliente: "))


descPorcentagem = desconto / 100
comisPorcentagem = comissao / 100
produtocomis = preco + comisPorcentagem


comissaoFinal = preco * comisPorcentagem
descontoFinal = descPorcentagem * produtocomis
precoFinal = produtocomis - descontoFinal

print('O preço com a comissão vai ficar: ', produtocomis)
print('A comissão do vendedor é de:', comissaoFinal)
print('O desconto do cliente é de:', descontoFinal)
print('O preco final ficará em:', precoFinal)
