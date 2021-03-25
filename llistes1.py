alumnes = []
notes = []
mitjana = 0
total = 0

while True:
    alumne = input("Alumne: ")
    if alumne == "fi":
        break
    if alumne in alumnes:
        print("Aquest alumne ja està registrat")
        continue
    
    nota = input("Nota: ")
    if nota == "fi":
        break

    alumnes.append(alumne)
    notes.append(float(nota))

for nota in notes:
    total += nota

mitjana = total / len(notes)

print(alumnes)
print(notes)
print("La mitjana és: " + str(mitjana))

while True:
    alumneNota = input("Quin alumne vols? ")
    if alumneNota not in alumnes:
        break
    
    print(str(notes[alumnes.index(alumneNota)]))