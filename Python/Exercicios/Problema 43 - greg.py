vogais = ['A', 'E', 'I', 'O', 'U']
def verificaVogal(pPalavra):
    if pPalavra[0].upper() in vogais:
        print(f'A palavra {pPalavra} começa por uma vogal')
    else:
        print(f'A palavra {pPalavra} começa NÃO por uma vogal')
        return pPalavra

palavra = input("Digite uma palavra:")
print(verificaVogal(palavra))