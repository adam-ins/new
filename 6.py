diaNaix = int(input("Dia naixement: "))
mesNaix = int(input("Mes naixement: "))
anyNaix = int(input("Any naixement: "))

diaAct = int(input("Dia actual: "))
mesAct = int(input("Mes actual: "))
anyAct = int(input("Any actual: "))

if diaNaix == diaAct and mesNaix == mesAct:
    anys = anyAct - anyNaix
    print("Felicitats! Tens " + str(anys) + " anys.")