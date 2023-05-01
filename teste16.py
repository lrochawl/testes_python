  #Aprendendo utilizar TRY EXCEPT
# TRY analisa cada linha do codigo e direciona a aplicação para o EXCEPT ao localizar um erro

try:

    numero = input("Digite um numero ")
    print("Analisando o numero")
    numero = float(numero)
    print("Duplicando o numero....")
    numero_duplicado = numero * 2
    print(f"O resultado é {numero_duplicado}")

except:
    print("Erro ao duplicar o numero")
