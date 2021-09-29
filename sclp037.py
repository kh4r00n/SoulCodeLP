# 5) Fazer um programa para encontrar todos os múltiplos de 3 de 1 a 50.

cont = 0
num = 1

while num <= 50:
    if num % 3 == 0:
        cont += 1
        print(num)
    num += 1

print(f'Existem {cont} números multiplos de 3 entre 1 e 50')
