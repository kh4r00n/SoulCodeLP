#7) Faça um programa que leia 5 idades e mostre na tela a média das idades lidas.

cont = 1
soma = 0

while cont <=5:
  idade = int(input('Digite uma idade: '))

  while idade <= 0 or idade > 120:
    idade = int(input('Idade inválida! Informe uma idade entre 1 e 120: '))
  soma += idade
  cont += 1

media = soma / 5

print(f'A média das idades é igual a: {media}')