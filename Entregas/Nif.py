# Python1 - Anem de compres
# Calcular DNI (Part opcional)
lletres = "TRWAGMYFPDXBNJZSQVHLCKE" 
n = int(input("Quants NIFs vols introduir? (Entre 1-10): "))

i = 1
if n <= 10:
    while i <= n:
        nif = int(input("NIF número " + str(i) + ": "))
        modulNif = nif % 23
        print("El DNI número " + str(i) + " és " + str(nif) + str(lletres[modulNif]))
        i += 1
else:
    print("El número de NIFs ha de ser entre 1 i 10")