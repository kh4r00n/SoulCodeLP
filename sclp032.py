# Faça um algoritimo que obrigue o usuario a digitar 10 numeros negativo
# Mostre o numero negativo na tela


cont = 1

while cont <= 10:
    num = float(input('Digite um numero negativo: '))

    while num >= 0:
        num = float(input('Número inválido! Digite um numero negativo: '))

    print(num)
    cont += 1
