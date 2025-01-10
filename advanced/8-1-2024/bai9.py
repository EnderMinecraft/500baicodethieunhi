num = input('number: ')
numlist = num.split()
sum = 0
for i in range(len(numlist)):
    sum = sum + float(numlist[i])
print(sum)