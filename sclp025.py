'''Crie um programa que peça uma letra como entrada se a letra digitada for diferente de A
imprima "Tente novamente" e se a letra digitada correta imprima "Agora você acertou
'''

letra = str(input('Digite: '))

while letra != 'A':

  letra = str(input('Tente novamente: '))

print('Agora você digitou certo')