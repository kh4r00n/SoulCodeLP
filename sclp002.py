'''Crie um programa que leia dos valores e printe a adição, multiplicação, divisão e subtração deles'''

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo número: '))

adic = n1 + n2
mult = n1 * n2
divi = n1 / n2
subt = n1 - n2

print(f'A divisão de {n1} e {n2} é igual a {divi:.2f}')
print(f'A multiplicação de {n1} e {n2} é igual a {mult:.2f}')
print(f'A adicão de {n1} e {n2} é igual a {adic:.2f}')
print(f'A subtração de {n1} e {n2} é igual a {subt:.2f}')