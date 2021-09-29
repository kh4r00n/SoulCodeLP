# 4) Fazer um programa para encontrar todos os números pares entre 1 e 100.

cont = 0
num = 1

while num <= 101:
    if num % 2 == 0:
        cont += 1
        print(num)
    num += 1

print(f'Existem {cont} números pares entr 1 e 100')
