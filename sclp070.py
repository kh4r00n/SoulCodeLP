#5) Faça um Programa que peça as quatro notas de 10 alunos junto com o seu nome.
#Calcule e armazene numa lista a média de cada aluno, bem como em outra lista armazene o nome do aluno.
#Ao final imprima o número de alunos com média maior ou igual a 7.0 junto com o seu nome.


alunos = []
media_alunos = []
soma = 0
quantidade = 0

for i in range(3):
  nome = str(input(f'Digite o nome do {i+1}ª aluno: '))
  for n in range(4):
    nota = float(input(f'Digite a {n+1}ªdo aluno {nome}: '))
    while nota <0 or nota >10:
      nota = float(input(f'Digite a {n+1}ªdo aluno {nome}: '))

    soma += nota

  media = soma / 4

  alunos.append(nome)
  media_alunos.append(media)
  soma = 0

print('-' * 30)
print('Alunos com nota maior ou igual a 7: ')
for cont in range(len(alunos)):
  if media_alunos[cont] >= 7:
    print(f'{alunos[cont]}: {media_alunos[cont]}')
    quantidade +=1

print(f'A quantidade de alunos com media maior ou igual a 7 é de {quantidade}')
