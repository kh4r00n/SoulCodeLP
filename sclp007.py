'''Crie um programa quea leia o salario e despesas de uma pessoa e inform a porcentagem que a despesa representa de seu salário'''


salario = float(input('Iforme seu salário: '))
despesa = float(input('Informe suas despesas: '))

porc = (despesa * 100) / salario

print(f'Sua despesas de {despesa:.2f} equivale a {porc}% do seu salário de R${salario:.2f}')