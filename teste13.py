#Formatação de de fstring

#padding
variavel = 'ABCD'

print(f'{variavel: >10}.') #prenche os espaços da esquerda para direita até somar 10 caracters
print(10 * '-')
print(f'{variavel: <10}.') #prenche os espaços da direita para esquera até somar 10 caracters
print(10 * '-')
print(f'{variavel: ^10}.') #prenche os espaços até somar 10 caracters colocando o conteudo da string o mais proximo do centro
print(f'{variavel:$^10}.') #pode ser utilizado outros caracteres para preenchimento
