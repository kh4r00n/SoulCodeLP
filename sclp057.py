#8) Escreva um programa em Python para encontrar o fatorial de qualquer número.
#FAT 5 = 5 x 4 x 3 x 2 x 1 = 120

f = 1
num = int(input('Digite um número: '))

while num <1:
  num = int(input('Digite um número: '))

for c in range(1, num+1, 1):
  f = f*c

print(f'O fatorial de {num} é {f}')