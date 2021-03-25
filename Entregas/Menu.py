plats = []
preus = []
platsUsuari =[]
preuTotal = 0
i = 0

print("Introdueix els plats i els preus del restaurant:")
while True:
    plat = input("Plat: ")
    if plat == "fi":
        break
    preu = input("Preu de '" + plat + "': ")
    if preu == "fi":
        break

    plats.append(plat)
    preus.append(int(preu))

print("\n---- " "MENÚ", "----\n")
for plat in plats:
    i += 1
    print(str(i) + " - " + plat, end = "")
    print(" - " + str(preus[plats.index(plat)]) + "€")
print("\n-- " "0 - PAGAR", "--\n")

while True:
    comanda = int(input("Què volen dinar? "))

    if comanda == 0:
        break

    platsUsuari.append(plats[comanda-1])
    preuTotal += preus[comanda-1]

print("\nAquesta és la teva comanda:\n---------------------------")
for platUsuari in platsUsuari:
    print(" - " + platUsuari)
print("---------------------------\nTotal: " + str(preuTotal) + "€")