#getinput
m=int(input("Nhập số người nộp hồ sơ M="))
n = input("Nhập thời gian từng người chờ=")
k =int(input("Nhập người thứ k="))
#split
splited = n.split()
splited = list(map(int, splited))
k1 = k-1
sub = 0
sum = 0
for i in splited:
    if (sub==k-1):
        pass
    else:
        sum = i+sum
        sub=sub+1
    

#result
print(f"Người thứ {k} phải đợi {k1} người nữa")
print(f"Thời Gian chờ là {sum} phút")
input()