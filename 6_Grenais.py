c = 0
grenais = 1
emp = 0
inter = 0
gremio = 0
entrada2 = 0
#----------------------------------
gi, gg = map(int, input().split()) #1ºgrenal
if gi > gg:
    inter += 1
elif gg > gi:
    gremio += 1
elif gg == gi:
    emp += 1
#-----------------------------------------------
print ("Novo grenal (1-sim 2-nao)")
entrada = int(input())
#-----------------------------------------------
if entrada == 1:
    while entrada == 1:
        gi, gg = map(int, input().split())
        grenais += 1
        if gi > gg:
          inter += 1
        elif gg > gi:
            gremio += 1
        elif gg == gi:
            emp += 1
        print ("Novo grenal (1-sim 2-nao)")
        entrada2 = int(input())
        if entrada2 == 1:
            entrada += 0
        elif entrada2 == 2:
            entrada += 1
        else: 
            entrada += 0
#-------------------------------------------------
print (f"{grenais} grenais")
print (f"Inter:{inter}") 
print (f"Gremio:{gremio}")
print (f"Empates:{emp}")
#-------------------------------------------------
if gremio > inter:
    print ("Gremio venceu mais")
elif inter > gremio:
    print ("Inter venceu mais")
elif inter == gremio:
    print ("Nao houve vencedor")