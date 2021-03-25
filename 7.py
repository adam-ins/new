lletres = "TRWAGMYFPDXBNJZSQVHLCKE"

while True:
    nif = int(input("NIF: "))
    lletra = input("Letra DNI: ")
    modulNif = nif % 23

    if lletres[modulNif] == lletra:
        print("Correcte.")
        break
    else:
        print("Incorrecte. Torna a provar.")