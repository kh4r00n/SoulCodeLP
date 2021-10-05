#3) Faça um Programa que leia 4 notas de alunos e armazene-as dentro de uma lista. 
# Em seguida mostre as notas e a média das notas na tela.

notas = []
n = 4 
total = 0

for c in range(0, n):
  nota = -1
  while nota < 0 or nota >10:
    nota = float(input(f'Digite a {c+1}ª nota: '))
  notas.append(nota)
  total += nota

media = total / n

print(f'As notas do aluno são: {notas} e a média é: {media:.2f}')