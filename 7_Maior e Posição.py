c = 0
sub = 0
quando = 0
#----------------------
while c < 100: 
    c += 1
    n = int(input())
    if n > sub:
        sub = n
        quando = c
#----------------------
print (sub)
print (quando)