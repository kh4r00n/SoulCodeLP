#3) Utilizando a estrutura de repetição for, faça um programa em Python que receba 10 números
#e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo,
#escrevendo estas informações.#

intervalo = 0

for c in range(1, 11, 1):
  n = int(input('Digite um valor: '))
  if n <10 or n >20:
    intervalo += 1

print(f'Existem {intervalo} fora do intervalo 10-20')