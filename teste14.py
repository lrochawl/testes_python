#fatiamento de string
#[inicio:fim:passo] 
#em python geralmente o indice final não é incluido
# se o passo for -1 inverte a string
#len conta a quantidade de caracters

variavel = "Olá mundo"

print(len(variavel)) #mostra o tamanho da atring
print(variavel[0:len(variavel):2]) # mostra a string com passo de dois em dois caracters
print(variavel[::-1]) #inverte a string