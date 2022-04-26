num = int(input())

if num % 2 == 0:
    impar = num - 1
    par = num + 2
else:
    impar = num - 2
    par = num + 1
    
print(impar, par)
