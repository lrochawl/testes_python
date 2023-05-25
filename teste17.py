#PYTHON não tem o conceito de constantes
#para melhorar a leitura do codigo if's com muitas condições podem ser separados em outros blocos

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
n = input("Digite um numero inteirio ")


#  pode ser utilizado também if (n.isdigit()): para verificar se foi digitado um numero inteiro


try:
    n = int(n)
    if((n % 2 == 0) == True):
        print(f"{n} é Par")
    else:
        print(f"{n} é impar")

except:
    print(f"{n} não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
data = input("Que horas são: ")
 
try:

    hora = int(data)

    if(hora >= 0 and hora <= 11):
        print("Bom dia")
    elif(hora >= 12 and hora <= 17):
        print("Boa tarde")
    elif(hora >= 18 and hora <= 23):
        print("Boa noite")
    else:
        print("Não conheço essa hora")

except:
    print(f"{data} não é um numero")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


nome = input("Qual o seu nome: ")

tamanho = len(nome)
if(tamanho > 2 ):
    if(tamanho <= 4):
        print("Seu nome é curto")
    elif(tamanho >= 5 and tamanho <= 6):
        print("Seu nome é normal")
    # elif(tamanho > 6 ):
    else:
        print("Seu nome é muito grande")
else:
    print("Digite pelo menos uma letra")        