import random
grp = ['văn', 'toán', 'lý', 'hóa', 'sinh', 'anh']

a = range(2, 8)
az = []
for i in a:
    z = random.choice(grp)
    grp.remove(z)
    az.append(i)
    az.append(z)
    print(az)
    az.clear()
input()   
    