#PROBLEMA 43 - VERIFICA VOGAL
#Criar uma função que receba um palavra como argumento e retorne uma resposta do tipo texto caso a primeira letra da palavra
#seja uma vogal (minúscula ou maiúscula), conforme respostas abaixo:
#1) “A palavra começa por uma vogal.”
#2) “A palavra NÃO começa por uma vogal.”
#Além disso, realizar o teste da função com palavras a serem digitadas pelo usuário.

vogais = ['A', 'E', 'I', 'O', 'U']
def verificaVogal(pPalavra):
    if pPalavra[0].upper() in vogais:
        return "A palavra começa por uma vogal."
        
    else:
        return "A palavra NÃO começa por uma vogal."

palavra = input("Digite uma palavra:")
print(verificaVogal(palavra))

    