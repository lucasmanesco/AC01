c = str(input())
p = int(input())
dias = ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado')

d = dias.index(c)+p

if d > 6:
    d = d - 7
    
if p == 0:
    print(f'chega hoje!')
else:
    print(f'sera entregue {dias[d]}')
