preco = float(input('Digite preço do produto: '))
quantidade = int(input('Digite quantidade comprada: '))

valor = preco * quantidade
desconto = 0.9 - (0.01 * quantidade)
valor_final = valor * desconto

print('Valor Total = R$%.2f' % valor)
print('Valor com Desconto = R$%.2f' % valor_final)
