media = 0
c = 0
c2 = 0
#----------------------------------------
while c != 1:
    a = float(input())
    if a < 0 or a > 10:
        print ("nota invalida")
    else:
        c += 1

while c2 != 1:
    b = float(input())
    if b < 0 or b > 10:
        print ("nota invalida")
    else:
        c2 += 1
#---------------------------------------
media = (a + b) / 2
#---------------------------------------
print (f"media = {media:.2f}")