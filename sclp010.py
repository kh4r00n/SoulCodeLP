'''Faça um programa que pergunte quanto a pessoa quer emprestado, faça o cálculo do empréstimo a juros  compostos. Para fazer o empréstimo solicite:
    – Quanto ela quer emprestado?
   – Em quantos meses ela vai pagar?
       *A Taxa de juros será de 2% ao mês.
     Segue a fórmula dos Juros compostos:   M = C x (1+i)^t    ‌
    M é o valor final após a aplicação dos juros
    C o valor que a pessoa vai pegar emprestado
     i é a taxa de juros
     t é o tempo'''

empre = float(input('Informe o valor do emprestimo '))
meses = int(input('Em quantos meses pretende pagar: '))

m = empre * ((1+ 0.02) ** meses)

print(f'O valor final a ser pago é de: R$ {m:.2f}')