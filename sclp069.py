#5) Faça um Programa que peça as quatro notas de 10 alunos junto com o seu nome.
#Calcule e armazene numa lista a média de cada aluno, bem como em outra lista armazene o nome do aluno.
#Ao final imprima o número de alunos com média maior ou igual a 7.0 junto com o seu nome.

nomes = []
media = []

for c in range(0, 4, 1):
  nome = str(input('Digite seu nome: '))
  nomes.append(nome)
  for x in range(4):
    nota = float(input(f'Digite {c+1}ª nota: '))
    while nota < 0 or nota > 10:
        print('Nota inválida! Digite uma nota entre 0 e 10: ')
        nota = float(input(f'Digite {c+1}ª nota: '))
    nota += nota
    m = nota / 4
    media.append(m)

print(nomes)
print(media)
