import random
num = random.randrange(100)
intents = 0
intentsPermesos = 6
i = 0

print("He generat un número del 0 al 100 i l'has d'endevinar.")

while True:
    intents += 1
    if intents > intentsPermesos:
        print("Ho sento, ja no et queden més intents.")
        exit()

    numInput = int(input("El teu número: "))

    if numInput == num:
        break

    # Pista
    if numInput > num:
        pista = "El teu número és més gran que el generat."
    else: 
        pista = "El teu número és més petit que el generat."
    print("Incorrecte. Pista: " + pista)

print("Correcte. Ho has endevinat en " + str(intents) + " intents.")