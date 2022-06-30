subTotal = 0 #muito importante, para acumular os valores dos produtos
print('Bem vindo(a) a Lanchonete da Kathleen O. B. de Lima')
print(  17 * '*', 'CARDÁPIO', 17 * '*')
print('''| Código |       Descrição        | Valor |
|  100   |   Cachorro Quente      | 9,00  |
|  101   | Cachorro Quente Duplo  | 11,00 |
|  102   |       X - Egg          | 12,00 |
|  103   |      X - Salada        | 12,00 |
|  104   |       X - Bacon        | 14,00 |
|  105   |       X - Tudo         | 17,00 |
|  200   |  X - Refrigerante Lata |  5,00 |
|  201   |      X Chá Gelado      |  4,00 |''')
while True: #laço para repetir as perguntas caso o usuário queira continuar
        pedido = input('Entre com o código desejado: ')
        if pedido == '100':
            subTotal = subTotal + 9.00
        elif pedido == '101':
            subTotal = subTotal + 11.00
        elif pedido == '102':
            subTotal = subTotal + 12.00
        elif pedido == '103':
            subTotal = subTotal + 12.00
        elif pedido == '104':
            subTotal = subTotal + 14.00
        elif pedido == '105':
            subTotal = subTotal + 17.00
        elif pedido == '200':
            subTotal = subTotal + 5.00
        elif pedido == '201':
            subTotal = subTotal + 4.00
        #if e elif para identificar o código desejado pelo usuário e apresentar o valor
        else:
        #else para caso o usuário digite algo diferente do esperado que está dentro do if e elif e apresentar o print abaixo
            print('Opção inválida. Tente novamente!')
            continue #para voltar ao início do laço while
        print('O valor a ser pago está em {:.2f}'.format(subTotal))
        #print para ir mostrando o valor atualizado a cada escolha do usuário
        resposta = int(input('Deseja pedir mais alguma coisa? \n1 - Sim \n0 - Não \n>> '))
        if resposta == 1:
            continue #para voltar ao início do laço
        else:
            print('O total a ser pago é: R${:.2f}'.format(subTotal))
            break #Para sair do laço while e encerrar o programa




