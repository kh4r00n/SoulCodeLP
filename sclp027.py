'''
Crie um programa que informe quantos números pares existem entre 50 e 220
'''

cont = 0
num = 50

while num <= 220:
  if num % 2 == 0:
    cont += 1
  num += 1

print(f'Existem {cont} números pares entre 50 e 220')