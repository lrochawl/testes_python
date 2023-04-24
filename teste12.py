#interpolação python
# s  - string
#d e i - int
#f - float
#x e X - Hexadecimal

nome =  'Lucas'
preco = 100.95255
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('- ' * 10)
print('O hexadecimal de %s é %08X' % (nome, int(preco)))