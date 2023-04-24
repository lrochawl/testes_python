#trinando estrutura de controle condicional 

primeiro_valor = input('Digite o primeiro numero: ')
segundo_valor  = input('Digite o segundo numéro: ')

if primeiro_valor >= segundo_valor:
    resultado = f'{primeiro_valor=} é maior ou igual ao {segundo_valor=}'
    print(resultado)
else:
    resultado = f'{segundo_valor=} é maior que {primeiro_valor=}'
    print(resultado)