#Questão 1 - Biblioteca Senai (2 pontos)
#OBJETIVO:
#A biblioteca do Senai necessita de um sistema para o controle de devoluções de livros.
#Inicialmente, é necessário um programa que possa ler o nome do livro, o código do livro,
#o tipo de usuário (professor ou aluno) e a quantidade de dias que o livro
#ficou emprestado (conforme o exemplo abaixo).
#Portanto, desenvolva um algoritmo para resolver o problema proposto.

#REQUISITOS:
#a)Considerar que o professor tem 20 dias para devolver o livro e o aluno tem 10 dias.
#Caso o usuário entregue o livro dentro do prazo, o programa deve informar: “Devolução realizada com sucesso”. Em caso de atraso, o programa deverá calcular a multa (R$ 1,50 por dia) e exibir o texto conforme exemplo abaixo. (1 ponto)
#b)Caso seja informado um tipo de usuário diferente de professor (“P” ou “p”) ou aluno (“A” ou “a”), o programa deverá informar “Tipo de usuário desconhecido!” e encerrar a execução. (1 ponto)

print("Bem vindo ao programa da Biblioteca Senai!!")

# ----------------- ENTRADA DE DADOS----------------
nomeLivro = input("Digite o nome do Livro: ")
codLivro = int(input("Digite o código do Livro: "))
tipoUsuario = str(input("Digite o tipo de usuário: "))
diasEmprestimo = int(input("Digite a quantidade de dias que o livro ficou emprestado: "))
# --------------------------------------------------

# ----------------- PROCESSAMENTO/SAÍDA----------------
if tipoUsuario == "A" or tipoUsuario == "a":
    if diasEmprestimo <= 10:
        print("Devolução realizada com sucesso.")
    else:
        multa = (diasEmprestimo - 10) * 1.5
        print("Para os alunos, o prazo limite de empréstimo é de 10 dias, portanto a multa devida é de R$", multa)
elif tipoUsuario == "P" or tipoUsuario == "p":        
    if diasEmprestimo <= 20:
        print("Devolução realizada com sucesso.")
    else:
        multa = (diasEmprestimo - 20) * 1.5
        print("Para os Professores, o prazo limite de empréstimo é de 20 dias, portanto a multa devida é de R$", multa)
        
else:
    print("Tipo de usuário desconhecido!") #item b
# ----------------- PROCESSAMENTO/SAÍDA----------------