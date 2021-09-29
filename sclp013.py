'''Crie um programa que compare os números e printe na tela se eles são iguais e qual o menor e o maior número'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))

if n1 == n2:
  print(f'{n1} e {n2} são iguais')
elif n1 > n2:
  print(f'{n1} é o maior número')
else:
  print(f'{n2} é o maior número')