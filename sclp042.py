# 8) Ler 10 números e informar na tela quantos números pares foram digitados e quantos números ímpares foram digitados.
par = 0
impar = 0
cont = 1

while cont <= 10:
    num = int(input('Digite um numero negativo: '))

    if num % 2 == 0:
        par += 1
    else:
        impar += 1

    cont += 1

print(f'Foram digitados {par} números pares e {impar} números ímpares')

