#estrutura de controle de fluxo if else
#precisa verificar a correta marcação do codigo

condicao_1 = False
condicao_2 = False
condicao_3 = True

if condicao_1: #condição falsa não executada
    print('Condição 1 executada')
elif condicao_2: #condição falsa não executada
    print('Condição 2')
else: #condição de escape executada
    print('Não foram encontradas condições validas')

if condicao_3: #condição verdadeira executada
    print('Condição 3 executada')
else: #condição não executada
    print('Codigo encerrado')