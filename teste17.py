#PYTHON não tem o conceito de constantes
#para melhorar a leitura do codigo if's com muitas condições podem ser separados em outros blocos

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
n = input("Digite um numero inteirio ")

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
hora = input("Que horas são")


if(hora >= 0 and hora <= 11):
    print("Bom dia")
elif(hora >= 12 and hora <= 17):
    print("Boa tarde")
elif(hora >= 18 and hora <= 23):
    print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""



hora_ini, minuto_ini, hora_final, minuto_final = (int (x) for x in input().split() )

hora_ini = hora_ini * 60 + minuto_ini
hora_final = hora_final * 60 + minuto_final

duracao_jogo = hora_final - hora_ini

if(duracao_jogo <= 0):
    duracao_jogo = 24 * 60 - duracao_jogo

minutos = duracao_jogo % 60
horas = duracao_jogo // 60

print("O JOGO DUROU "+str(horas)+" HORA(S) E "+str(minutos)+" MINUTO(S)")

javascript, java, c++, python, php