n = int(input())
a = 0
drentro = 0
frora = 0
#-----------------------------
for i in range (1, n + 1, 1):
    a = int(input())
    if a >= 10 and a <= 20:
        drentro += 1
    else: 
        frora += 1
#-----------------------------
print (f"{drentro} in")
print (f"{frora} out")
        