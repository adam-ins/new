quantitat = 0
nota = 0
total = 0
mitjana = 0

nota = int(input("Nota #" + str(quantitat) + ": "))
while nota >= 0:
    quantitat += 1
    total += nota
    nota = int(input("Nota #" + str(quantitat) + ": "))

mitjana = total / quantitat
print("Mijana = " + str(round(mitjana, 1)))