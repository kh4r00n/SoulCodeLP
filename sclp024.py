'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
'''

salario = float(input('Digite seu salário: '))

if salario <= 280.00:
  por = 0.2 * salario
  resultado = salario + por
  print (f'Seu salário antes do reajuste: R$ {salario}')
  print (f'Percentual aumentado: em 20%')
  print (f'O valor do aumento é: R$ {por}')
  print (f'Com o reajuste, o seu salário é: R$ {resultado}')

elif salario > 280 and salario <= 700:
  por = 0.15 * salario
  resultado = salario + por
  print (f'Seu salário antes do reajuste: R$ {salario}')
  print (f'Percentual aumentado: em 15%')
  print (f'O valor do aumento é: R$ {por}')
  print (f'Com o reajuste, o seu salário é: R$ {resultado}')

elif salario > 700 and salario <= 1500:
  por = 0.10 * salario
  resultado = salario + por
  print (f'Seu salário antes do reajuste: R$ {salario}')
  print (f'Percentual aumentado: em 10%')
  print (f'O valor do aumento é: R$ {por}')
  print (f'Com o reajuste, o seu salário é: R$ {resultado}')
else:
  por = 0.05 * salario
  resultado = salario + por
  print (f'Seu salário antes do reajuste: R$ {salario}')
  print (f'Percentual aumentado: em 5%')
  print (f'O valor do aumento é: R$ {por}')
  print (f'Com o reajuste, o seu salário é: R$ {resultado}')
