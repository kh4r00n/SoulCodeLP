55  # 1) Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.

numeros = []

for c in range(0, 5, 1):
    num = int(input('Digite um número: '))
    while num < 0:
        num = int(input('Digite um número: '))

    numeros.append(num)

print(numeros)