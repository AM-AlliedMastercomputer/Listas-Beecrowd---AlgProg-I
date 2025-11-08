n = 0
c = 0
soma = 0
#---------------------------
for i in range (1, 7, 1):
    n = float(input())
    if n > 0:
        soma += n
        c += 1
#---------------------------
media = soma / c
print (f"{c} valores positivos")
print (f"{media:.1f}")