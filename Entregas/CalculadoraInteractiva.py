# PRIMER EXERCICI (OBLIGATORI I PART OPCIONAL)
# Adam Feo Funes - 2n SMX B

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

while True:
    oper = input("Operació (+, -, *, /, %): ")
    if oper == "+":
        resultat = num1 + num2
        break
    elif oper == "-":
        resultat = num1 - num2
        break
    elif oper == "*":
        resultat = num1 * num2
        break
    elif oper == "/":
        resultat = num1 / num2
        break
    elif oper == "%":
        resultat = num1 % num2
        break
    else:
        print("Operació invàlida. Torna a indicar la operació desitjada.")
        continue

print("El resultat és " + str(resultat))