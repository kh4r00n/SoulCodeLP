#3) Faça um Programa que leia 4 notas de alunos e armazene-as dentro de uma lista.
# Em seguida mostre as notas e a média das notas na tela.

notas = list()
totNotas = media = 0
for c in range(4):
    nota = float(input(f'Digite {c+1}ª nota: '))
    while nota < 0 or nota > 10:
        print('Nota inválida! Digite uma nota entre 0 e 10: ')
        nota = float(input(f'Digite {c+1}ª nota: '))
    notas.append(nota)
totNotas = sum(notas[::])
media = totNotas /len(notas)
print(' ------------------ BOLETIM ------------------')
print(f'Notas: {notas} | Média Final: {media:.2f}')