n1 = int(input())
robo1 = n1
n2 = int(input())
robo2 = n2
soma = 0
#-------------------------------------------
if n1 > n2:
    for n1 in range (n1, n2, -1):
        if n1 % 2 == 1:
                if n1 == robo1:
                     soma += 0
                else: 
                     soma += n1
elif n2 > n1:
    for n2 in range (n2, n1, -1):
        if n2 % 2 == 1:
                if n2 == robo2:
                     soma += 0
                else: 
                     soma += n2
else:
    soma = 0
#-------------------------------------------
print (soma)