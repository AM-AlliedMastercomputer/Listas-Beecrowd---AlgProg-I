n = int(input())
c = 0
divisão = 0
#-----------------
while c != n:
    a, b = map(float, input().split())
    if b == 0:
        print ("divisao impossivel")
    else:
        divisao = a / b 
        print (f"{divisao:.1f}")
    c += 1