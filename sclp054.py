#5) Crie um programa em Python que leia N números (N digitado pelo usuário) e
#mostre na tela a soma e a média de todos os números lidos.

soma =  0
num = int(input('Digite quantos valores deseja saber a soma e media'))

while num <1:
  num = int(input('Valor inválido. Digite Novamente: '))

for c in range(1, num+1, 1):
  n1 = float(input(f'Digite o {c}º número: '))
  soma += n1

media = soma / num

print(f'A soma dos valores digitados é de: {soma} e a média é: {media}')
