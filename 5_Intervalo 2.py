n =  int(input())

inn = 0
out = 0
c = 0
x = 0
soma = 0

while c < n:
    x = int(input())
    if x >= 10 and x <= 20:
        inn += 1
    out = n - inn
    c += 1

print (f"{inn} in")
print (f"{out} out")