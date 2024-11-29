def work():
    o = open("xau.inp", "r")
    content = o.readlines()
    n=content[0]
    a = n.count('1')
    b = n.count('2')
    c = n.count('3')
    d = n.count('4')
    e = n.count('5')
    f = n.count('6')
    g = n.count('7')
    h = n.count('8')
    i = n.count('9')
    l = n.count('0')
    final = a+b+c+e+f+g+h+i+l
    print(final)
    count = ""
    for c in n:
        if c.isdigit():
            count = count + c
    def getSum(count):
        sum = 0
        for digit in str(count): 
          sum += int(digit)      
        return sum
    count = getSum(count)
    print(count)
    result = ''.join([i for i in n if not i.isdigit()])
    print(result)
    print("")
    input("Press Enter to continue.")
work()
