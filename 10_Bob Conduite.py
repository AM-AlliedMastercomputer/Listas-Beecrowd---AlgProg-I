t = int(input())
cond = 0
#--------------------------------------
while t != 0:
    r1, r2 = map(int, input().split())
    r1 = r1 * 2 #obtendo o diametro
    r2 = r2 * 2 #obtendo o diamtetro
    cond = (r1 + r2) // 2
    print (cond)
    t -= 1
#--------------------------------------
    
