acumulador = 0
print('Bem-vindo a Loja de gelados do Davi!')

while True:
    # while True, para só encerrar o programa quando o usuário tiver pedido tudo.
    while True:
        # while True para garantir que o usuário digite o sabor válido.
        sabor = input('Entre com o sabor desejado (CP/AC): ').upper()
        if sabor == 'CP' or sabor == 'AC':
            break
        else:
            print('Sabor inválido. Tente novamente.\n')
    while True:
        # while para garantir que o usuário digite o sabor válido.
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
        if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
            break
        else:
            print('Tamanho inválido. Tente novamente.\n')

    if sabor == 'CP':  # if e elif para as diferentes combinações de sabores e tamanhos.
        if tamanho == 'P':
            acumulador += 9
        elif tamanho == 'M':
            acumulador += 14
        elif tamanho == 'G':
            acumulador += 18
    elif sabor == 'AC':
        if tamanho == 'P':
            acumulador += 11
        elif tamanho == 'M':
            acumulador += 16
        elif tamanho == 'G':
            acumulador += 20

    print(f'Você pediu um {sabor} no tamanho {tamanho}\n'.replace('CP', 'Cupuaçu').replace('AC', 'Açaí'))
    # usei o método replace, para transformar a abreviação AC e CP em Açaí e Cupuaçu, para melhor visualização do usuário.

    continuar = input('Deseja pedir mais alguma coisa? (S/N): ').lower()
    # se o usuário quiser pedir mais, continue para voltar ao inicio do looping. Ou break para sair.
    if continuar == 's':
        continue
    elif continuar == 'n':
        break

print(f'\nValor total a ser pago: R${acumulador:.2f}')
