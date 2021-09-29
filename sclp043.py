# 9) Faça um programa que leia 3 notas (de 0 a 10) e informe na tela a média das notas lidas.

cont = 1
soma = 0

while cont <=3:
  nota = int(input('Digite sua nota: '))

  while nota <= 0 or nota > 10:
    nota = int(input('Idade inválida! Informe uma idade entre 1 e 10: '))
  soma += nota
  cont += 1

media = soma / 3

print(f'A média das idades é igual a: {media}')

