# Python1 - Anem de compres
# Calcular DNI (Part obligatòria)
lletres = "TRWAGMYFPDXBNJZSQVHLCKE"

nif = int(input("NIF: "))
preu = float(input("Preu: "))
descompte = float(input("Tant per cent de descompte: "))
iva = float(input("Tant per cent d'IVA : "))

preuDescompte = preu - (preu * (descompte/100))
preuFinal = preuDescompte + (preuDescompte * (iva/100))

modulNif = nif % 23
print("El teu DNI és " + str(nif) + str(lletres[modulNif]))
print("El preu final és de " + str(preuFinal) + "€")
