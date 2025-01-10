inp = int(input("Decimal to binary: "))
out = ""
while inp > 0:
    out = str(inp % 2) + out
    inp = inp // 2
print(out)