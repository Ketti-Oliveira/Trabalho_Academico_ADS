#--------- COMEÇO DA FUNÇÃO DEMENSOESOBJETO ---------

def dimensoesObjeto():
# Definição e codificação da função

    while True:
    #Função utilizada para repetir a pergunta caso ultrapasse o volume permitido
        try:
        # Função utilizada para repetir a pergunta caso o usuário digite algo diferente

            comprimento = float(input('Digite o comprimento do objeto (em cm): '))
            largura = float(input('Digite a largura do objeto (em cm): '))
            altura = float(input('Digite a altura do objeto (em cm): '))
            volume = (comprimento * largura * altura)
            print('O volume do objeto é (em cm³): {}'.format(volume))
            if volume < 1000:
                return 10.00
            elif 1000 <= volume < 10000:
                return 20.00
            elif 10000 <= volume < 30000:
                return 30.00
            elif 30000 <= volume < 100000:
                return 50.00
            else:
                print('Não aceitamos objetos com dimensões tão grandes.')
                print('Por favor, entre com as dimensões desejadas novamente, dentro do limite permitido!')
            continue
        except ValueError:
        #Função para reconhecer caso seja digitado algo inesperado, mandando assim para o continue
            print('Você digitou alguma dimensão do objeto com valor não numérico.')
            print('Por favor entre com as dimensões desejadas novamente.')
            continue
            #continue é para repetir

#------------ FIM A FUNÇÃO DIMENSOESOBJETO ----------
#-------------- COMEÇO DA FUNÇÃO PESOOBJETO ---------
def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em Kg): '))
            if peso <= 0.1:
                return 1
            elif 0.1 < peso <= 1:
                return 1.5
            elif 1 < peso <= 10:
                return 2
            elif 10 < peso <= 30:
                return 3
            else:
                print('Não aceitamos objetos tão pesados!\nPor favor entre com o peso desejado novamente.')
                continue
        except ValueError:
            print('Você digitou o peso do objeto com valor não numérico.\nPor favor entre com o peso desejado novamente.')


#----------------- FIM A FUNÇÃO PESOOBJETO ----------
#-------------- COMEÇO DA FUNÇÃO ROTAOBJETO ---------
def rotaObjeto():
    while True:
        rota = input('''Selecione a rota:\nSP - De São Paulo para o Paraná\nPS - De Paraná para São Paulo
SR - De São Paulo para o Rio de Janeiro\nRS - De Rio de Janeiro para São Paulo\nSB - De São Paulo para Bahia
BS - De Bahia para São Paulo\n>> ''')
        if rota == 'SP':
            return 1
        elif rota == 'PS':
            return 1
        elif rota == 'SR':
            return 1.2
        elif rota == 'RS':
            return 1.2
        elif rota == 'SB':
            return 1.5
        elif rota == 'BS':
            return 1.5
        else:
            print('Você digitou uma rota que não existe.\nPor favor entre com a rota desejada novamente!')
            continue


#----------------- FIM A FUNÇÃO ROTAOBJETO ----------
#-------------------- COMEÇO DA FUNÇÃO MAIN ---------
print('Bem vindo(a) à Companhia de Logística Kathleen O. B. de Lima S.A.')
dimensaoObj = dimensoesObjeto()
pesoObj = pesoObjeto()
rotaObj = rotaObjeto()

print('Total a pagar(R$): {:.2f} '.format(dimensaoObj * pesoObj * rotaObj), end='')
print('(dimensões: {:.0f} * peso: {} * rota: {})'.format(dimensaoObj, pesoObj, rotaObj))
#---------------------- FIM A FUNÇÃO MAIN ----------



