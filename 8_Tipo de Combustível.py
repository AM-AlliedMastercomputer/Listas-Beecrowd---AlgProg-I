x = 0
c = 0
alcol = 0
gasolina = 0
diesel = 0
#--------------------------------
while c == 0:
    x = int(input())
    if x == 1:
        alcol += 1
    elif x == 2:
        gasolina += 1
    elif x == 3:
        diesel += 1
    elif x == 4:
        c += 1
    else: 
        c += 0
#-------------------------------
print ("MUITO OBRIGADO")
print (f"Alcool: {alcol}")
print (f"Gasolina: {gasolina}")
print (f"Diesel: {diesel}")
