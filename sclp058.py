# 9) Escreva um programa em Python que leia um número inteiro positivo e diga se o número informado é primo.

num = int(input('Digite um numero positivo: '))
tot = 0

while num < 1:
    num = int(input('Digite um numero positivo: '))

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1

print(f'O numero {num} foi divisível {tot} vezes')

if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')