c = 0
pos = 0
soma = 0
med = 0
mediaf = 0

while c < 6:
    x = float(input())
    if x > 0:
        soma += x
        pos += 1
        med += 1
    c += 1

mediaf = soma / med
print (f"{pos} valores positivos")
print (f"{mediaf:.1f}")