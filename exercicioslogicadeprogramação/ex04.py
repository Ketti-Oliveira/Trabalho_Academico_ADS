listaPecas = []
#------------ COMEÇO DA FUNÇÃO cadastrarPeca ----------
def cadastrarPeca(codigo): #função definida para o cadastramento de peças
    print('Bem vindo(a) ao CADASTRAR peças')
    print('A peça a ser cadastrada é {}'.format(codigo))
    nome = input('Por favor entre com o NOME da peça: ')
    fabricante = input('Por favor entre com o FABRICANTE  da peça: ')
    valor = float(input('Por favor entre com o VALOR(R$) da peça: '))
    dicionarioPeca = {'codigo'   : codigo, #dicionário para guardar as peças e características descrita pelo usuário
                      'nome' : nome,
                      'fabricante' : fabricante,
                      'valor': valor}
    listaPecas.append(dicionarioPeca.copy()) #lista para ir buscar as palavras dentro do dicionário
                                            #para poder usar nas próximas funções
#------------ FIM DA FUNÇÃO cadastrarPeca ------------
#------------ COMEÇO DA FUNÇÃO consultarPeca ----------
def consultarPeca(): #função criada para consultar as peças
    while True: #inicio do laço para repetir as opções do menu
        try: #try e o except value error para caso o usuário digite algo inesperado
            print('Bem vindo(a) ao CONSULTAR peças')
            opConsultar = int(input('Escolha a opção desejada:\n'
                                    '1 - Consultar Todas as Peças\n'
                                    '2 - Consultar Peças por Código\n'
                                    '3 - Consultar Peças por Fabricante\n'
                                    '4 - Retornar\n'
                                    '>> '))
            if opConsultar == 1:
                print('Você selecionou a opção CONSULTAR TODAS AS PEÇAS')
                for pecas in listaPecas: #selecionar cada dicionário da minha lista (cada peça da lista de peças)
                    for key, value in pecas.items(): #selecionar cada conjunto chave/valor do dicionário ex('nome' : pedivela)
                        print('{} : {}'.format(key,value))
            elif opConsultar == 2:
                print('Você selecionou a opção CONSULTAR PEÇAS POR CÓDIGO' )
                codigo = int(input('Digite o CÓDIGO da peça: '))
                for pecas in listaPecas:
                    if(pecas['codigo'] == codigo):
                        for key, value in pecas.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 3:
                codigo = input('Digite o FABRICANTE da peça: ')
                for pecas in listaPecas:
                    if (pecas['fabricante'] == codigo):
                        for key, value in pecas.items():
                            print('{} : {}'.format(key, value))
                print('Voce selecionou a opção CONSULTAR PEÇAS POR FABRICANTE')
            elif opConsultar == 4:
                return
            else:
                print('Essa opção não existe no menu. Tente novamente!')
            #if elif e else para devolver ao usuário a resposta da opção desejada
                continue
                #continue para voltar ao inicio do laço
        except ValueError:
            print('Você digitou valores não numéricos. Tente novamente!')


#------------ FIM DA FUNÇAO consultarPeca-------------
#------------ COMEÇO DA FUNÇÃO removerPeca ------------
def removerPeca(): #funão criada para a remoção de peças criadas
    print('Bem vindo(a) ao REMOVER peças')
    codigo = int(input('Digite o Código da Peça a ser REMOVIDA: '))
    for pecas in listaPecas: #para ir buscar dentro da lista e em seguida do dicionário
        if pecas['codigo'] == codigo: #para explicitar o que vai ser buscado dentro do dicionário
            listaPecas.remove(pecas) #função para remover a peça escolhida pelo usuário
#------------ FIM DA FUNÇÃ  O removerPeca ---------------
#--------------- COMEÇO DA FUNÇÃO MAIN -----------------
print('Bem vindo(a) ao controle de estoque da Bicicletaria da Kathleen O. B. de Lima')
registroEstoque = 0
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n'
                          '1 - Cadastrar Peças\n'
                          '2 - Consultar Peças\n'
                          '3 - Remover Peças\n'
                          '4 - Sair\n>> '))
        if opcao == 1:
            registroEstoque = registroEstoque + 1
            cadastrarPeca(registroEstoque)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Obrigado por utilizar o nosso Controle de Estoque. Volte sempre!')
            break
        else:
            print('Essa opção não existe no menu. Tente novamente!')
    except ValueError:
        print('Você digitou valores não numéricos. Tente novamente!')
#------------------ FIM DA FUNÇÃO MAIN -----------------


