num = int(input("Số hs = ? "))
hs = []
ca = 0
for c in range(1, num+1):
    hs.append(input(f"Họ tên hs {c} : "))
for i in range(len(hs)):
    if "Hương" in str(hs[i]):
        ca = 1
if ca == 1:
    print("Có học sinh tên Hương")
else:
    print("Không có học sinh nào có tên Hương")