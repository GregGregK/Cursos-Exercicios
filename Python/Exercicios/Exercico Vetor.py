preco = 0.72
gasto = 0
gMedia = 0
cMedia = 0
consumos = []
gastos = []
for consumo in range(12):
    cConsumo = int(input('Digite o consumo mensal: '))
    consumos.append(consumo)
    gasto = consumos[consumo]*preco
    gastos.append(gasto)

for i in range(12):
    print('gasto no mês' +str(i+1)+':'+ str(round(gastos[i],2)))


