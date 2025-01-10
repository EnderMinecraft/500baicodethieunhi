i = "-1 2 3 1 -54 1 2 -1 3 1 2 -2 2 8 34 -2 -5 -2"
i = i.split()
result = []
for n in i:
    if int(n) >= 0:
        result.append(n)
print(result)