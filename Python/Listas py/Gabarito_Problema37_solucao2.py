#PROBLEMA 37 - PROFISSÕES

vNome=[]
vProfissao = []
vProfissaoUnica = []
vProfissaoUnicaConta = [0,0,0,0,0,0]

for i in range(6):
    nome = input("Por favor digite o nome da pessoa " + str(i + 1) + ":")
    profissao = input("Por favor digite a profissão da pessoa " + str(i + 1) + ":")
    vNome.append(vNome)
    vProfissao.append(profissao)
print(vProfissao)

#Cria vetor com profissões
for i in range(6):
    profissaoUnica = vProfissao[i]
    if len(vProfissaoUnica) == 0:
        vProfissaoUnica.append(profissaoUnica)
    else:
        jaexiste = False
        for j in range(len(vProfissaoUnica)):
            if profissaoUnica == vProfissaoUnica[j]:
                jaexiste = True
                break
        if jaexiste == False: vProfissaoUnica.append(profissaoUnica)
            
print(vProfissaoUnica)


#Conta Profisssões
for i in range(len(vProfissaoUnica)):
    for j in range(len(vProfissao)):
        if vProfissaoUnica[i]==vProfissao[j]:
            vProfissaoUnicaConta[i]+=1
print(vProfissaoUnicaConta)

#Mostra Informações
for i in range(len(vProfissaoUnica)):
    print("Profissão:" + vProfissaoUnica[i] + ", Pessoas:" + str(vProfissaoUnicaConta[i]))

