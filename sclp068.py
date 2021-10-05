#4) Faça um Programa que leia 20 números inteiros e armazene-os numa lista.
#Em seguida, crie mais 2 listas, uma para armazenar os números pares e outra para armazenar os números impares.
#Ao final, Imprima as três listas.

num = []
par = []
impar = []

for c in range (0, 20, 1):
  n = int(input('Digite um número: '))

  num.append(n)

  if n % 2 == 0:
    par.append(n)
  else:
    impar.append(n)

print(f'Lista com os 20 números: {num}')
print(f'Lista com os números pares: {par}')
print(f'LIsta com os números ímpares: {impar}')