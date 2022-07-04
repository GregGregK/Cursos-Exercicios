#QUESTÃO 1 - MÉDIA DA TURMA (3 PONTOS)
#Considere o caso em que para um aluno ser aprovado em uma disciplina, é preciso que ele
#possua nota igual ou superior a média da turma. Sendo assim, desenvolva uma algoritmo em
#Python que receba as notas de 5 alunos. Após isso, o programa deverá informar:
#a) A média da turma (1,5 ponto).
#b) Situação do aluno 1 (primeira nota)  APROVADO OU REPROVADO (1,5 ponto).
#Obs.: Para este exercício, deverá ser utilizada uma estrutura de repetição (while ou for) para
#obter os valores do usuário.

nota = 0
somaNotas = 0
notaAluno1 = 0

for i in range(1,6):
    nota = float(input("Digite a nota do aluno " +  str(i) + ":"))
    somaNotas = somaNotas + nota #soma notas
    if i == 1: notaAluno1 = nota #Armazena a nota do primeiro aluno em uma outra variável
    
mediaNotas = somaNotas / 5 #Calcula média
print("\nMédia da turma:" + str(mediaNotas)) #exibe média

if notaAluno1>=mediaNotas: #verifica se nota do aluno 1 é maior ou igual a média da turma
      print("Portanto, o aluno 1 está APROVADO!")
else:
      print("Portanto, o aluno 1 está REPROVADO!")
    

