n = int(input())
divisão = 0
#-----------------
for i in range (1, n + 1, 1):
    a, b = map(float, input().split())
    if b == 0:
        print ("divisao impossivel")
    else:
        divisao = a / b 
        print (f"{divisao:.1f}")