def calculo (a, b, c):
    regra3 = ((a * b) * 100) / c
    Vlado = regra3 ** 0.5
    return Vlado
#---------------------------------------------------
for i in range (1, 1000000):
    inp = input()
    if(inp == "0"):
        break
    #------------------------------------
    a, b, c = map(int, inp.split())
    #------------------------------------
    resultado = calculo(a, b, c)
    resto = resultado // 1
    print (f"{resto:.0f}")