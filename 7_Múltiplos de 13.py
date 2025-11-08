x = 0
y = 0
soma = 0
#----------------------
x = int(input())
y = int(input())
#----------------------
if x < y:
    while x <= y:
        if x % 13 != 0:
         soma += x
        x += 1
    print (soma) 
elif y <= x:
    while y < x:
        if y % 13 != 0:
          soma += y
        y += 1
    print (soma)
elif x == y:
    if x % 13 != 0:
        soma += x + y  
    print (soma)