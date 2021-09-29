'''Preço dos produtos'''

price = float(input('Informe o preço do produto: '))
print('1 - A Vista em dinheiro ou cheque 10% de desconto')
print('2 - A Vista no cartão de crédito, recebe 15% de desconto')
print('3 - Em duas vezes, preço normal de etiqueta sem juros')
print('4 - Em três vezes, preço normal de eiqueta mas juros de 10%')
pag = int(input('informe a opção de pagamento: '))

if pag == 1:
    price -= price * 0.10
    print(f'O preço final é de: R$ {price} ')

elif pag == 2:
    price -= price * 0.15
    print(f'O preço final é de: R$ {price} ')

elif pag == 3:
    print(f'O preço final é de: R$ {price} ')

elif pag == 4:
    price += price * 0.10
    print(f'O preço final é de: R$ {price} ')

else:
    print('Opção de pagamento inválida')