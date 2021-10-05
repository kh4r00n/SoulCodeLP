#7) Faça um Programa que leia uma lista A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos da lista.

#Usando map & reduce & lambda
f = []

for c in range(0, 3, 1):
  num = int(input('Digite 1 número: '))
  f.append(num)

print(f'Os números lidos foram: {f}')

from functools import reduce

k = list(map(lambda x: x**2, f))

print(f'O quadrado dos números lidos é: {k}')

s = reduce(lambda x, y: x+y, k)

print(f'A soma dos quadrados dos números lidos é: {s}')
