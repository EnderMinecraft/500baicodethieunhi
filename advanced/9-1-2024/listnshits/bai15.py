A = [1,2,3,"4",5,6,7,8,9,10]
i = 3
v = 11
for i in range(len(A)):
    if i == 3:
        A.insert(i,v)
        break
print(A)