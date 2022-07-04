nMedia = 0
notas = []
for nNotas in range(5):
    aNota = int(input('Digite a nota: '))
    notas.append(aNota)
    nMedia = sum(notas)/len(notas)
print(nMedia)

if notas[0] >= nMedia:
    print(f'O aluno 1 foi aprovado com a nota{notas[0]} e a média da turma foi{nMedia}')
else:
    print('reprovado')