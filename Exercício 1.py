print('Bem-vindo a Loja do Davi!')
v = float(input('Informe o valor do produto: '))
quantidade = int(input('Informe a quantidade do produto: '))
valor = quantidade*v
print(f'Valor SEM desconto: R${valor:.2f}')
if valor < 2500:
    print('Valor menor que 2500, 0% de desconto.')
#Eu APLICAREI a fórmula de desconto quando eu for printar o valor com desconto.
elif valor >= 2500 and valor < 6000: #Se o valor for igual ou maior que 2500 e menor que 6000
    print(f'Valor COM desconto: R${valor - (valor * 0.04):.2f}')
elif valor >= 6000 and valor < 10000: #Se valor for igual ou maior que 6000 e menor que 10000
    print(f'Valor COM desconto: R${valor - (valor * 0.07):.2f}')
else: #Se valor for igual ou maior que 10000:
    print(f'Valor COM desconto: R${valor - (valor * 0.11):.2f}') 