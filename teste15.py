#Exercicio dos utimos teste

nome = input('Digite seu nome ')
idade = input('Digite sua idade ')

if(nome != "" and idade != ""):
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if(nome.find(" ") == True):
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espços")
    if(nome.find("n") == True):
        print("Seu nome possui letra 'N' ")
    else:
        print("Seu nome não possui letra 'N' ")
    print(f"A primeira letra do seu nome é '{nome[0]}'")
    print(f"A ultima letra do seu no é {nome[len(nome)-1]}")
else:
    print("Desculpe, você deixou campos vazios.")