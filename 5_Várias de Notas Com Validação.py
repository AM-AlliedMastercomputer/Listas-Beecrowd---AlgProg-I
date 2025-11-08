#DEFININDO FUNÇÕES-----------------------
def Media (x):
    media = x / 2
    return media 
#DEFININDO VARIÁVEIS---------------------
NotaB = 0
NotaA = 0
resposta = 0
continuar = 0
c = 0
Soma = 0
media = 0
#CODIGO PRINCIPAL------------------------
while c == 0:
 #VERIFICAÇÃO DA 1ºNOTA------------------
 while True:
    Soma = 0
    NotaA = float(input())
    if NotaA < 0 or NotaA > 10:
        Soma += 0
        print ("nota invalida")
    elif NotaA >= 0 or NotaA <= 10:
        Soma += NotaA
        break
 #VERIFICAÇÃO DA 2ºNOTA-------------------
 while True:
    NotaB = float(input())
    if NotaB < 0 or NotaB > 10:
        Soma += 0
        print ("nota invalida")
    elif NotaB >= 0 or NotaB <= 10:
        Soma += NotaB
        break
 #IMPRIMINDO A MEDIA---------------------
 resultado = Media(Soma)
 print (f"media = {resultado:.2f}")
 #LOOP PARA RECEBER A RESPOSTA------------
 while continuar == 0:
   print ("novo calculo (1-sim 2-nao)")
   resposta = int(input())
   if resposta == 1:
    break 
   elif resposta == 2:
    c += 1
    break
   elif continuar != 1 or continuar != 2:
      continuar == 0