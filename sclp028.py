'''
Crie u programa que leia um número de 3 dígitos
'''

num = int(input('Digite um número: '))

while num < 100 or num > 999:
  num = int(input('O numero nao tem 3 digitos. Digite novamente:'))