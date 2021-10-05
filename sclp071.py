#6) Faça um Programa que leia uma lista de 5 números inteiros. Após, percorra a lista e
#calcule a soma e a multiplicação dos números.  Ao final, mostre os números lidos, a soma dos números e a multiplicação entre eles.

#Usando Reduce
f = []

for c in range(0, 5, 1):
  num = int(input('Digite um número: '))
  f.append(num)

print(f'Os números lidos foram: {f}')

from functools import reduce

somas = reduce(lambda x, y: x+y, f)
print(f'A soma dos números lidos é: {somas}')

multis = reduce(lambda x, y: x*y, f)
print(f'A multiplicação dos números lidos é: {multis}')