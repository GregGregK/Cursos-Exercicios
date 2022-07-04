#PROBLEMA 44 - VERIFICA VOGAIS E CONSOANTES

#Desenvolver um algoritmo que retorne a quantidade de vogais e consoantes de uma determinada palavra.
#Exemplo:
#O usuário digita palavra ALGORITMO.
#Resposta: A palavra ALGORITMO possui 4 vogais e 5 consoantes.
#Dica: Criar funções retorna_nro_vogais() e retorna_nro_consoantes() para retornar a quantidade
# de vogais/consoantes com base nas palavras informadas.

def retorna_nro_vogais(pPalavra):
    contarVogais = 0
    vogais = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(pPalavra)):
        if pPalavra[i].upper() in vogais: contarVogais = contarVogais + 1
    return contarVogais

def retorna_nro_consoantes(pPalavra):
    contarConsoantes = 0
    consoantes = ['B', 'C', 'D', 'F', 'G','H',
                  'J', 'K', 'L', 'M','N', 'P',
                  'Q', 'R', 'S','T', 'V', 'X', 'Y','W', 'Z']
    for i in range(len(pPalavra)):
        if pPalavra[i].upper() in consoantes: contarConsoantes = contarConsoantes + 1
    return contarConsoantes

palavra = input("Digite uma palavra:")
totalVogais = retorna_nro_vogais(palavra)
totalConsoantes = retorna_nro_consoantes(palavra)
print(f'A palavra {palavra} possui {totalVogais} vogal e {totalConsoantes} consoantes')


            
            
