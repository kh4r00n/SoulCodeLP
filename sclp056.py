#7) Faça um programa que receba um número positivo digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado.
# Por exemplo, se o usuário inseriu 4, a saída deve ser 10 (1+2+3+4=10).

soma = 0

num = int(input('Digite um número: '))

while num <1:
  num = int(input('Digite um número: '))

for c in range(num, 0, -1 ):
  soma += c

print(f'A soma de todos os números de 1 até {num} é igual a = {soma}')
