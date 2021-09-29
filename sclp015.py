'''Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja diferente de um código
 armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a mensagem ‘Usuário inválido!’.
  Caso o Código seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta
 (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a senha esteja correta, deve ser
 mostrada a mensagem ‘Acesso permitido’.'''

cod1 = int(input('digite um codigo: '))
cod2 = 1234
senha2 = 9999

if cod1 == cod2:
  senha1 = int(input('Digite sua senha: '))
  if senha1 == senha2:
    print('Senha Correta')
  else:
    print('senha incorreta')
else:
  print('usuario invalido')