quantitat = 0
nota = 0
total = 0
mitjana = 0

while True:
    nota = int(input("Nota #" + str(quantitat) + ": "))
    if nota < 0:
        break
    else:
        quantitat += 1
        total = total + nota

mitjana = total / quantitat
print("Mijana = " + str(round(mitjana, 1)))