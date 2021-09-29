'''Crie um programa que leia dois valores e faça a potenciação de x1 elevado a x2 e x2 elevado a x1'''

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo número: '))

expo1 = n1 ** n2
expo2 = n2 ** n1

print(f'{n1} elevado a {n2} é igual a {expo1:.2f}')
print(f'{n2} elevado a {n1} é igual a {expo2:.2f}')