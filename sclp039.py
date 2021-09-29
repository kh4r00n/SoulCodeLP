# 6) Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido. versão 2:

valor = int(input('Digit um numero entre 1 e 10: '))
while valor <1 or valor >10:
  valor = int(input('Digit um numero entre 1 e 10: '))

cont = 1
while cont <= 10:
  print(f'{valor} x {cont} = {valor * cont}')
  cont += 1