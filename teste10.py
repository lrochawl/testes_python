#Operadores logiscos
#and (e) or (ou) not (não)
#and -  Todas as codições precisam ser verdadeiras
#Se qualquer valor for considerado for falso toda a expressão será considerada falsa
#também existe o tipo None que é utilizado para representar um não valor
#qualquer valor que for considerado como verdadeiro toda a expressão será considerada como verdadeira

entrada = input('[E] Entrar e [S] Sair: ')
senha_digitada = input('Digite sua senha: ')
senha_permitida = '1234'

if entrada == 'E' and senha_digitada == senha_permitida:
        print('Entrou')
elif((entrada == 'E' or entrada == 'e') and senha_digitada != senha_permitida): #utilizando operador Not que inverte o resultado da expressão
    print('Senha incorreta ')
else:
    print('Saiu')

print(bool(0)) #False
print(bool(0.0)) #False
print(bool(False)) #False

print(True and True and False) #False
print((True or True) and False) #False