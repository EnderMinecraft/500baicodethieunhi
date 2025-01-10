num = int(input("Số hs: "))
hs = []
dictl = [["buffer", "Đệm", "Tên"]]
for i in range(1, num+1):
    hs.append(input(f"Nhập tên học sinh {i}: "))
for n in range(len(hs)):
    dictl.append(list(str(hs[n]).split(" ")))
for i in range(len(dictl)):
    dictl[i].remove(dictl[i][0])
    dictl[i].reverse()
print("\n")
for row in dictl :
    for element in row:
        print(element, end=" ")
    print()