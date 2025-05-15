def escolha_servico(): #função para o funcionário escolher o serviço desejado
    while True:
        servico = input('\nEntre com o tipo de serviço desejado\n'
                        'DIG - Digitalização\n'
                        'ICO - Impressão Colorida\n'
                        'IPB - Impressão Preto e Branco\n'
                        'FOT - Fotocópia\n'
                        '>>').upper().strip()
        if servico in ('DIG', 'ICO', 'IPB', 'FOT'):
            break
        else:
            print('Escolha inválida, entre com o tipo de serviço novamente\n')
    return servico

def num_pagina(): #função para escolher o número de páginas
    while True:
        try:
            num = int(input('Entre com o número de páginas: '))
            if num < 20000:
                if num < 20:
                    # Sem desconto
                    return num
                elif num >= 20 and num < 200:
                    # Desconto de 15%'
                    return num * 0.85
                elif num >= 200 and num < 2000:
                    # Desconto de 20%
                    return num * 0.80
                elif num >= 2000 and num < 20000:
                    # Desconto de 25%
                    return num * 0.75

            else:
                print('Não aceitamos tantas páginas de uma vez.')
        except:
            print('Erro. Por favor, entre apenas com valor númerico.')

def servico_extra(): #função para escolher o serviço extra
    while True:
        try:
            extra = int(input('\nDeseja adicionar algum serviço?\n'
                              '1 - Encadernação Simples - R$ 15.00\n'
                              '2 - Encadernação Capa Dura - R$ 40.00\n'
                              '0 - Não desejo mais nada\n'
                              '>>'))
            if extra not in (1,2,0):
                print('Erro. Por favor, selecione apenas 1, 2 ou 0.')
            else:
                if extra == 1:
                    return 15
                elif extra == 2:
                    return 40
                if extra == 0:
                    return 0
        except:
            print('Erro. Por favor, entre apenas com valor númerico (1, 2 ou 0).')


print('Bem vindo a Copiadora do Davi Franklin de Melo')

servico = escolha_servico()
pagina = num_pagina()
extra = servico_extra()
total = 0 #variável acumuladora, para receber o valor total que o cliente pagará

#implementando o total a pagar:
if servico == 'DIG':
    # R$1.10
    total = (1.10 * pagina) + extra
elif servico == 'ICO':
    # R$1.00
    total = (1.00 * pagina) + extra
elif servico == 'IPB':
    # R$0.40
    total = (0.40 * pagina) + extra
elif servico == 'FOT':
    # R$0.20
    total = (0.20 * pagina) + extra

#print para mostrar o total, e os serviços selecionados, para melhor visualização:
print(f'Total: R${total:.2f} (serviço: {servico} * páginas: {pagina:.0f} + extra: {extra:.2f})'
      .replace('DIG', '1.10')
      .replace('ICO', '1.00')
      .replace('IPB', '0.40')
      .replace('FOT', '0.20'))