inp = input("Dãy số: ")
inp = inp.split()
x=0
for i in range(len(inp)):
    x += int(inp[i])
print(f"Tổng dãy số: {x}")
print(f"Trung bình cộng dãy số: {x/len(inp)}")
print(" ".join(inp))