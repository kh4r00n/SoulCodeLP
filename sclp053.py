#4) Escreva um programa que leia um valor correspondente ao número de jogadores de um time de vôlei.
#O programa deverá ler uma altura para cada um dos jogadores e, ao final, informar a altura média do time.

mediaAltura = 0

for i in range(1, 7, 1):
  alt = float(input(f'Informe a altura do jogador {i}: '))
  mediaAltura += alt

media = mediaAltura / i

print(f'A média de altura do time é de: {media}')