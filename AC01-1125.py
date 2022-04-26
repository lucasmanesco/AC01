nota_trabalho = float(input())
nota_prova = float(input())

media = (0.5 * nota_trabalho) + (0.5 * nota_prova)

if media >= 6:
    print('aprovado')
else:
    if nota_trabalho >= 2:
        print('talvez com a sub')
    else:
        print('reprovado')
