a = float(input('how many? : '))
if a < 5:
    price = a * 12000
    print(price)
elif a >= 5:
    price = a * 10000
    print(price)
else:
    print("Wtf man?")