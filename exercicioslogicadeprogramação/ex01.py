print('Bem vindo(a) a loja da Kathleen Oliveira Bernardino de Lima')
valor = float(input('Entre com o valor do produto: ')) #variável para armazenar o valor
quantidade = int(input('Entre com a quantidade: ')) #variável para armazenar a quantidade
subTotal = valor * quantidade # variável para armazenar o resultado que será aplicado o desconto
if 0 <= quantidade < 10: # se a quantidade for entre 0 e 9 entra nesse if não dando desconto
    valorFinal = subTotal
elif 10 <= quantidade < 100: # se a quantidade for entre 10 e 99 entre nesse elif dando desconto de 5%
    valorFinal = subTotal - subTotal * 0.05
elif 100 <= quantidade < 1000: # se a quantidade for entre 100 e 999 entra nesse elif dando desconto de 10%
    valorFinal = subTotal - subTotal * 0.10
else: #se a quantidade for maior ou igual a 1000 entra nesse else dando desconto de 15%
    valorFinal = subTotal - subTotal * 0.15
print('O valor sem desconto foi: R${:.2f}'.format(subTotal))
print('O valor com desconto foi: R${:.2f}'.format(valorFinal))
#valorFinal é uma variável criada para armazenar o resultado calculando o desconto
