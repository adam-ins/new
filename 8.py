while True:
    any = int(input("Any: "))
    if any % 400 == 0:
        print("Sí")
    elif any % 100 == 0:
        print("No")
    elif any % 4 == 0:
        print("Sí")
    else:
        print("No")