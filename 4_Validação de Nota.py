media = 0
#----------------------------------------
for i in range (1, 10000000):
    a = float(input())
    if a < 0 or a > 10:
        print ("nota invalida")
    else:
        break

for i in range (1, 10000000):
    b = float(input())
    if b < 0 or b > 10:
        print ("nota invalida")
    else:
        break
#---------------------------------------
media = (a + b) / 2
#---------------------------------------
print (f"media = {media:.2f}")