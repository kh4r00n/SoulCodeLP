'''Escreva um programa que leia ym número de 3 dígitos e printe o valor invertido'''

num = int(input('Digite um numero de 3 digitos: '))

centena = num // 100
dez = (num%100) // 10
unidade = num%10

print(f'O valor invertido de {num} é: {unidade}{dez}{centena}')