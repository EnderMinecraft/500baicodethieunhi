n = int(input("n = ?"))
arr , z, sum= [], 0, 0
for digit in list(str(n)):
    arr.append(digit)
while z < len(str(n)):
    sum = int(arr[z]) + sum
    z = z + 1
print(sum)