i = int(input("Số hs=? "))
hs = []
for x in range(i):
    hs.append(input("Họ tên hs: "))
hs.reverse()
print(" ".join(hs))