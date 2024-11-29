def work():
    o = open("dayso.inp", "r")
    content = o.readlines()
    n=content[1]
    result = ''.join([i for i in n if i.isdigit()])
    def getSum(n):
        sum = 0
        for digit in str(n): 
            sum += int(digit)      
        return sum
    print(getSum(result))
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
    if (a!=0):
        print("1:%d" %(a))
    if (b!=0):
        print("2:%d" %(b))
    if (c!=0):
        print("3:%d" %(c))
    if (d!=0):
        print("4:%d" %(d))
    if (e!=0):
        print("5:%d" %(e))
    if (f!=0):
        print("6:%d" %(f))
    if (g!=0):
        print("7:%d" %(g))
    if (h!=0):
        print("8:%d" %(h))
    if (i!=0):
        print("9:%d" %(i))
    if (l!=0):
        print("0:%d" %(l))
    print("")
    input("Press Enter to continue.")
work()

