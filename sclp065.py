#3) Faça um Programa que leia 4 notas de um alunos e armazene-as dentro de uma lista.
#Em seguida mostre as notas e a média das notas na tela.

notas = []

for c in range(4):
  n = float(input(f'Digite a {c+1}º nota: '))
  notas.append(n)
  while n <0 or n >10:
    n = float(input(f'Nota. Inválida. DIgite novamente. Digite a {c+1}º nota: '))
    notas.append(n)
print(f'As suas notas foram {notas[0]}, {notas[1]}, {notas[2]}, {notas[3]}')

snotas = sum(notas)

media = snotas / len(notas)

print(f'Sua média é: {media}')
