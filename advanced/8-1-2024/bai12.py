num = int(input("Số hs = ? "))
hs = []
ca = 0
for c in range(1, num+1):
    hs.append(input(f"Họ tên hs {c} : "))
fin = input("Nhập tên hs cần tìm: ")
for i in range(len(hs)):
    if fin in str(hs[i]):
        ca += 1
print(ca)