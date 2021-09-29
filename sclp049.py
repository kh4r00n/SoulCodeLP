#Faça um algotirimo que leia um numero positivo e
#Imprima na tela todos os divisores desse número
#Ex: 16 - 1, 2, 4, 8, 16
#Ex: 27 - 1, 3, 9, 27

num = int(input('Digite um número positivo: '))

while num <1:
  num = int(input('Digite um número positivo: '))

for c in range(1, num +1):
  if num % c == 0:
    print(f'{c}')
