items = ["Lechuga", "Tomate", "Pepino", "Pan", "Agua", "Pimientos"]
preus = [1, 2, 3, 4, 5, 6]

for item in items:
    print(item, end = " ")
    print(str(preus[items.index(item)]) + "€")

while True:
    producte = input("Quin producte vols? ")
    if producte not in items:
        break
    print("El producte \"" + producte + "\" costa " + str(preus[items.index(producte)]) + "€")