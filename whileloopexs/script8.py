i = 0
x = 1
while x <= 100:
    i = i+1
    if i % 10 == 0:
        print(str(x) + ' ')
    else : print(str(x) + ' ', end='')
    x = x+1