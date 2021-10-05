# 1) Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.
numeros = []

num = numeros.append(int(input('Digite um número: ')))

for c in range(0, 5, 1):
    # com append conta de 0, 1, 2, 3, 4, 5 - 6 vezes6
    num = numeros.append(int(input('Digite um número: ')))

print(numeros)
