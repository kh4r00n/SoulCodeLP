#Faça um algoritmo que leia 10 números entre 100 e 500 e mostre na tela  maior e o menor número. Versão 2:

i = 1

while i <= 10:
    num = int(input('Digite um numero entre 100 e 500: '))

    while num < 100 or num > 500:
        num = int(input('O numero nao não esta entre 100 e 500. Digite novamente:'))

    if i == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    i += 1

print(f'O menor numero é {menor} e o maior númeor é {maior}')