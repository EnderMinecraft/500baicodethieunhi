x = 0
arr = []
while x < 100:
    if x % 5 == 0 or x % 3 == 1:
        arr.append(x)
    x = x + 1
print(len(arr))
