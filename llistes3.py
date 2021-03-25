despeses = 0
ingressos = 0
llDespeses = []
llIngressos = []

diners = float(input("Quants diners tens?"))

while True:
    operacio = input("Vols (i)ngresar o (g)astar?")
    if operacio == "i":
        ingres = float(input("Quants vols ingressar?"))
        diners += ingres
        ingressos += ingres
        llIngressos.append(ingres)
        llDespeses.append("             ")
        print("Tens " + str(diners) + "€.")
        print("Has ingressat un total de " + str(ingressos) + "€.")
    elif operacio == "g":
        cost = float(input("Quants has gastat?"))
        diners -= cost
        despeses += cost
        llIngressos.append("            ")
        llDespeses.append(cost)
        print("Tens " + str(diners) + "€.")
        print("Has gastat un total de " + str(despeses) + "€.")
    else:
        break
    if diners < 0:
        print("T'has gastat més dels que tens")
        break

print("Ingressos    Despesses")
for ingres in llIngressos:
    print(ingres, "", llDespeses[llIngressos.index(ingres)])