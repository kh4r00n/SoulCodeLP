''' Escreva um programa para ler o ano de nascimento de uma pessoa e
escrever uma mensagem que diga se ela poderá ou não votar este ano
(não é necessário considerar o mês em que ela nasceu).  '''

from datetime import date
atual = date.today().year
nasc = int(input('Informe seu ano de nascimento: '))
idade = atual - nasc

if idade >= 16 and idade <18:
  print(f'Você tem {idade} anos e o voto é facultativo para você este ano')
elif idade >=18 and idade < 70:
  print(f'Você tem {idade} anos e o voto é obrigatório para você este ano')
else:
  print(f'Você tem {idade} anos e o voto é facultativo para você este ano')

