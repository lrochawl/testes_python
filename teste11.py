#Operadores in e not in
#Strings são iteraveis
# 0 1 2 [3] 4 5
# O t á [v] i o
#-6-5-4[-3]-2-1

nome = 'Otávio'
print(nome[3])
print(nome[-3])

print(10 * '-')
print('áa' in nome) #False
print('vio' in nome) #True

print(10 * '-')
print('vio' not in nome) #False
print('z' not in nome) #True

print('-' * 10)
nome = input('Digite um nome: ')
encontrar = input('O que deseja encontar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')

