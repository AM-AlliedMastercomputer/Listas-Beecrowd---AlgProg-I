x = 0
y = 0
soma = 0
#----------------------
x = int(input())
y = int(input())
#----------------------
if x < y:
    for x in range (x, y + 1):
        if x % 13 != 0:
         soma += x
    print (soma) 
elif y <= x:
    for y in range (y, x + 1):
        if y % 13 != 0:
          soma += y
    print (soma)
elif x == y:
    if x % 13 != 0:
        soma += x + y  
    print (soma)