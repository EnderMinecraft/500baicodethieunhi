A = [1,2,3,4,5,6,7,8,9,10]
i = 9
for n in range(len(A)):
    if n+1 == i:
        A.pop(A[n])
        break
print(A)