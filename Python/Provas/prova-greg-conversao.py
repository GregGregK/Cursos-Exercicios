print('Olá turista')
print('Vamos precisar da sua ajuda em algumas coisas, você irá precisar nos dizer a atual cotação do dolar. Se você quiser converter Real para dolar, digite RD. Se quiser converter Dolar para real Digite DR;')
dolar = float(input("Qual a atual cotação do dolár no momento?: "))
conversao = input("Qual o tipo de conversão? (RD, OU DR.): ")
valor = float(input("Digite o valor que deseja trocar: "))

if conversao == 'RD' or conversao == 'rd':
    conversaofinal = valor / dolar 
    print('Portanto, você tem direito a', conversaofinal)
elif conversao == 'DR' or conversao == 'dr':
    conversaofinal = dolar * valor
    print('Portanto, você tem direito a', conversaofinal)
else:
    print('invalido')





