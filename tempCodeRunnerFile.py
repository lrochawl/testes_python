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