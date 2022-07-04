notas=[]
media1=0
for i in range(5):
    notas.append(float(input("Digite a nota do aluno "+ str(i+1)+": ")))
    media1+= notas[i]
media2=media1/len(notas)
print("A média da turma é:",media2)
if notas[0] >= media2:
    print("Portanto, o aluno 1 está APROVADO!")
else:
    print("Portanto, o alino 1 está REPROVADO!")