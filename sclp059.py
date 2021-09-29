#10) Digitados dois números (base e expoente ), calcule o resultado  da potência
#utilizando apenas operadores básicos da matemática
#(soma, subtração, multiplicação ou divisão) e o comando FOR;

n1 = int(input('Digite a base: '))
n2 = int(input('Digite o expoente: '))

resp = 1
for c in range(n2):
  resp *= n1

print(resp)