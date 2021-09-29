#2) Em uma turma há 10 alunos. Cada aluno tem 2 notas. Um professor precisa calcular a média
#das duas notas de cada aluno. Crie um programa que resolva este problema.

for c in range(10):
  n1 = float(input('Digite a primeira nota: '))
  while n1 < 0 or n1 > 10:
    n1 = float(input('Nota inválida. Digite uma nota entre 0 e 10: '))

  n2 = float(input('Digite a segunda nota: '))
  while n2 < 0 or n2 > 10:
    n2 = float(input('Nota inválida. Digite uma nota entre 0 e 10: '))

  media = (n1 + n2) / 2

  print(f'A média do {c+1}º aluno foi {media}')
