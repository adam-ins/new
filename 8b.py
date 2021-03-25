any = int(input("Any: "))
while True:
    any += 1
    if any % 400 == 0:
        break
    elif any % 100 == 0:
        continue
    elif any % 4 == 0:
        break
    else:
        continue

print("El pròxim any de traspàs serà " + str(any))