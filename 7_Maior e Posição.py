n = 0
quando = 0
ultimo = 0 
#-----------------------------
for i in range (1, 101, 1):
    n = int(input())
    if n >  ultimo:
        ultimo = n
        quando = i
#-----------------------------
print (ultimo)
print (quando)