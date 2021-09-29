#6) Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7,
#mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.

sete = 0

for c in range(5, 101, 1):
  if c % 7 == 0 and c % 5 != 0:
    print(c)
    sete += 1

print(f'Existem {sete} números entre 5 e 100 que são divisiveis por 7 e não são multiplos de 5')