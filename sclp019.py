'''Desenvolva um algoritmo em Python para determinar o Índice de Massa Corporal (IMC) de uma pessoa.
Para fazer o cálculo do IMC basta dividir seu peso em quilogramas  (Kg) pela altura ao quadrado (em metros).
O número que será gerado deve ser comparado aos valores da tabela IMC, dada abaixo, para definir se você está abaixo, em seu peso ideal ou acima do peso.

< 16 - Magreza Grave
16 a < 17 - Magreza Moderada
17 a < 18,5 - Magreza Leve
18,5 a < 25 - Saudável
25 a < 30 - Sobrepeso
30 a < 35 - Obesidade Grau I
35 a < 40 - Obesidade Grau II(Severa)
>= 40 - Obesidade Grau III(Mórbida)'''

peso = float(input('Qual é seu peso?(kg)'))
altura = float(input('Qual a sua altura?(m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 16:
    print('Magreza Grave')
elif imc >= 16 and imc < 17:
  print('Magreza Moderada')
elif imc >= 17 and imc <18.5:
  print('Magreza Leve')
elif imc >= 18.5 and imc <25:
  print('Saudável')
elif imc >= 25 and imc < 30:
  print('Sobrepeso')
elif imc >= 30 and imc <35:
  print('Obesidade Grau I')
elif imc >= 35 and imc < 40:
  print('Obesidade Grau II(Severa)')
else:
  print('Obesidade Grau III(Mórbida)')