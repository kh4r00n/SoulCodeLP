'''Faça um Programa que pergunte em que turno você estuda.
Peça para digitar
M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

print('M - Matutino -- V - Vespertno ou N - Noturno')
turno = str(input('Informe seu turno: [M/V/N] ')).strip().upper()[0]

if turno not in 'MVN':
  print('Opção Inválida')
elif turno == 'M':
  print('おはよう')
elif turno == 'V':
  print('こんにちは')
else:
  print('こんばんは')
