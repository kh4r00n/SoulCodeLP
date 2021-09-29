'''Média com If/Else conceito A, B, C, D, E'''

n1 = float(input('Informe sua a nota da N1: '))
n2 = float(input('Informe sua a nota da N2: '))
n3 = float(input('Informe sua a nota da N3: '))

m = (n1+n2+n3)/3
ma = n1 + (n2*2) + (n3*3) + m / 7
#ma = n1 + n2*2 + n3*3 + m / 7


if ma >= 90:
  print(f'Sua Média é: {m:.2f} e sua Média de Aproveitamento é: {ma:.2f}. Parabéns Aprovado com conceito A')
elif ma >= 75 and ma <90:
  print(f'Sua Média é: {m:.2f} e sua Média de Aproveitamento é: {ma:.2f}. Parabéns Aprovado com conceito B')
elif ma >= 60 and ma <75:
  print(f'Sua Média é: {m:.2f} e sua Média de Aproveitamento é: {ma:.2f}. Parabéns Aprovado com conceito C')
elif ma >= 40 and ma <60:
  print(f'Sua Média é: {m:.2f} e sua Média de Aproveitamento é: {ma:.2f}. Reprovado com conceito D. Estude mais!')
else:
  print(f'Sua Média é: {m:.2f} e sua Média de Aproveitamento é: {ma:.2f}. Reprovado com conceito E. Estude mais!')