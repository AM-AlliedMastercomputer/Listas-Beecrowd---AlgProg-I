senha = 2002
tentativa = 0
#-----------------
for i in range (1, 10000000):
    tentativa = int(input())
    if tentativa == 2002:
        print ("Acesso Permitido")
        break
    else:
        print ("Senha Invalida")