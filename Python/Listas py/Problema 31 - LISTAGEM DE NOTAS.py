#PROBLEMA 31 - LISTAGEM DE NOTAS
#Criar um algoritmo que armazene o nome e duas notas de 5 alunos
#e imprima a listagem contendo nome, as duas notas e a média de cada aluno.

#declara vetores (vazios)
vNome  = []
vNota1 = []
vNota2 = []
vMedia = []
texto_saida = ""

#Entrada de Dados
for i in range(5):
    nome = input("Digite o nome do aluno " + str(i+1) + ":")
    nota1 = float(input("Digite a nota 1 nome do aluno " + str(i+1) + ":"))
    nota2 = float(input("Digite a nota 2 nome do aluno " + str(i+1) + ":"))
    vNome.append(nome)
    vNota1.append(nota1)
    vNota2.append(nota2)
    vMedia.append((nota1 + nota2)/2)
    print("\n")

#Saída de Dados
for i in range(len(vNome)):
    texto_saida += "Aluno:" + vNome[i] + "\t" + "Nota 1:" + str(vNota1[i]) + "\t"
    texto_saida += "Nota 2:" + str(vNota2[i]) + "\t" + "Média:" + str(vMedia[i]) + "\n"

print(texto_saida)