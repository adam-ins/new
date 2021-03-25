from datetime import datetime
avui = datetime.now()

diaNaix = int(input("Dia naixement: "))
mesNaix = int(input("Mes naixement: "))
anyNaix = int(input("Any naixement: "))

if diaNaix == avui.day and mesNaix == avui.month:
    anys = avui.year - anyNaix
    print("Felicitats! Tens " + str(anys) + " anys.")