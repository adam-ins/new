# SEGON EXERCICI (OPCIONAL)
# Adam Feo Funes - 2n SMX B

import random
import math

rNum1 = random.randint(0, 10)
rNum2 = random.randint(0, 10)

ops = ['+', '-', '*', '/']
rOp = ops[random.randint(0, 3)]

if rOp == "+":
    resultat = rNum1 + rNum2
elif rOp == "-":
    resultat = rNum1 - rNum2
elif rOp == "*":
    resultat = rNum1 * rNum2
elif rOp == "/":
    resultat = math.trunc(rNum1 / rNum2)

restposta = int(input("Quin és el resultat de la operació \"" + str(rNum1) + rOp + str(rNum2) + "\"?: "))

if restposta != resultat:
    print("Incorrecte, el resultat és: " + str(resultat))
else:
    print("Correcte!")