'''Faça um programa que pede duas notas de um aluno.
Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print(f'Tirando {n1:.2f} e {n2:.2f} a sua média é: {media:.2f} ')

if media == 10:
  print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')