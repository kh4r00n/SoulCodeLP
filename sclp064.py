#2) Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

numeros = []

for c in range(10):
  n = (float(input('Digite um número: ')))
  numeros.append(n)

numeros.reverse()

print(numeros)