#PROBLEMA 37 - PROFISSÕES

vNome=[]
vProfissao = []

vProfissaoUnica = []
vProfissaoUnicaConta = []

for i in range(6):
    nome = input("Por favor digite o nome da pessoa " + str(i + 1) + ":")
    profissao = input("Por favor digite a profissão da pessoa " + str(i + 1) + ":")
    vNome.append(vNome)
    vProfissao.append(profissao)

print(vProfissao)

#Cria vetor com profissões
for i in range(6):
    profissaoUnica = vProfissao[i]
    if profissaoUnica not in vProfissaoUnica: vProfissaoUnica.append(profissaoUnica)
print(vProfissaoUnica)

#Conta Profisssões
for i in range(len(vProfissaoUnica)):
    vProfissaoUnicaConta.append(vProfissao.count(vProfissaoUnica[i]))
print(vProfissaoUnicaConta)

#Mostra Informações
for i in range(len(vProfissaoUnica)):
    print("Profissão:" + vProfissaoUnica[i] + ", Pessoas:" + str(vProfissaoUnicaConta[i]))
