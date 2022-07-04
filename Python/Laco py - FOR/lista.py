listafamilia=[]
while True: 
    pessoafamilia=input('Digite o nome de uma pessoa da familia(0 se acabou)')
    if pessoafamilia == "0":
        break
    listafamilia.append(pessoafamilia)
for a in listafamilia:
    print(a)