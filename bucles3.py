import random
num = random.randrange(10)
encerts = 0
i = 0

print(num)
if num > 5:
    pista = "El número és més gran que 5"
else: 
    pista = "El número és més petit que 5"

numInput = int(input("El teu número: "))

while numInput != num:
    print("Incorrecte. Torna a provar. Pista: " + pista)
    numInput = int(input("El teu número: "))

print("Correcte. El número era " + str(num))