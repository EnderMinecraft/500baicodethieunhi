#import math 
#i ditched ext func 
num = input("num(2): ")
nlist = num.split()
nlist.sort()
def gcd(x: int, y: int):
    while y:
        x, y = y,x %y
    return abs(x)
print(gcd(int(nlist[0]), int(nlist[1])))