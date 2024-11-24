import math
a = float(input('a=? '))
b = float(input('b=? '))
c = float(input('c=? '))

def checkinenq(a, b ,c):
    pair1 = a - (b+c)
    pair2 = b - (a+c)
    pair3 = c - (a+b)
    
    if pair1 < 0 and pair2 < 0 and pair3 < 0:
        return 0
    else:
        print("not sastify inequation")

def calculate(a, b, c):
    if checkinenq(a, b, c) == 0:
        p = float(a + b + c)
        s = math.sqrt((p/2)*(p/2-a)*(p/2-b)*(p/2-c))
        print(f'Chu vi = {p}\nDiện tích = {s}')
    else:
        return 1
calculate(a, b, c)
