def work():
    a = input("a=?")
    l = len(a)
    print("Có %d chữ số" %(l))
    def getSum(a):
        sum = 0
        for digit in str(a): 
              sum += int(digit)      
        return sum
    b = getSum(a)
    print("Tổng các chữ số = %d" %(b))
    lis = list(a)
    f = max(lis)
    print("Chữ số lớn nhất = %s" %(f))
    print("")
    input("Press Enter to continue.")
work()

