#Operadores logiscos
#and (e) or (ou) not (não)
#and -  Todas as codições precisam ser verdadeiras
#Se qualquer valor for considerado for falso toda a expressão será considerada falsa
#também existe o tipo None que é utilizado para representar um não valor

entrada = input('[E] Entrar e [S] Sair: ')
senha_digitada = input('Digite sua senha: ')
senha_permitida = '1234'

if entrada == 'E' and senha_digitada == senha_permitida:
        print('Entrou')
elif(entrada == 'E' and senha_digitada != senha_permitida):
    print('Senha incorreta ')
else:
    print('Saiu')
