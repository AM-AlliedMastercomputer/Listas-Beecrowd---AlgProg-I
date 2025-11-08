x = int(input())
y = int(input())

#----------------
soma = 0
#----------------

if x > y:
    while x > y:
        x -= 1
        if x % 2 >= 1 and x != y:
            soma += x
    
print (soma)