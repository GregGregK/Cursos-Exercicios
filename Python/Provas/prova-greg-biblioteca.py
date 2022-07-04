print('Olá aluno, seja bem vindo ao sistema de retorno da biblioteca SENAI')
print('Vamos levar em consideração algumas coisas, se você é aluno seu tipo é "A", se você é professor seu tipo é "P", entendido?')
livro = input("Digite o nome do livro: ")
codigo = int(input("Digite o código do livro: "))
dias = int(input("Digite a quantidade de dias em que ficou com o(s) livro(s): "))
tipo= input("Digite o seu tipo de usuario (Lembrando A= Aluno , P= Professor): ")


multa = 1.50


if tipo == "A" or tipo =="a":
    if dias >= 10:
        diasA = dias - 10
        multado = multa * diasA
        print('Você foi multado o prazo para alunos é 10 dias, seu valor final está em R$:', multado)
    else:
        print("Devolução concluida com sucesso")
elif tipo == "P" or tipo == "p":
    if dias >=20:
        diasA = dias - 10
        multado = multa * diasA
        print('Você foi multado o prazo para professores é 20 dias, seu valor final está em R$:', multado)
    else:
        print("Devolução concluida com sucesso")
else:
    print("tipo invalido")


