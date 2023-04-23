#parametros nomeados
id = 1
a= 'A1 B2 C3'
b = 1.1
string = '{} a={number} b={id}'
print(string.format(id, id=a, number=b)) # ao nomear um parametro todos os outros a frente devem ser nomeados