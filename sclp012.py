'''Crie um programa que leia um número e informe se o número é par ou ímpar'''

num = int(input('Digite um número: '))

if num % 2 == 0:
  print(f'{num} é par')
else:
  print(f'{num} é ímpar')