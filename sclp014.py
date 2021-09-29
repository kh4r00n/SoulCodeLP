'''Preço do combustivel'''

litros = float(input('Informe a quantidade de litros que você deseja abastecer: '))
combustivel = (input('Digite \'A\' para Alcool e \'G\' para Gasolina: '))


litros = float(input('Informe a quantidade de litros que você deseja abastecer: '))
combustivel = (input('Digite \'A\' para Alcool e \'G\' para Gasolina: ')).lower().strip()

if combustivel == 'a' or combustivel == 'g':
    if combustivel == 'a':
      preco= litros * 5.2
      if litros <= 20:
        preco -= 5.2 * litros * 0.03
        print(f'O preço a pagar é R$ {preco:.2f}')
      else:
        preco -= 5.2 * litros * 0.05
        print(f'O preço a pagar é R$ {preco:.2f}')

    elif combustivel == 'g':
      preco = litros * 6.10
      if litros <= 20:
        preco -= 6.1 * litros * 0.04
        print(f'O preço a pagar é R$ {preco:.2f}')
      else:
        preco -= 6.1 * litros * 0.06
        print(f'O preço a pagar é R$ {preco:.2f}')
else:
    print('opção invalida')
