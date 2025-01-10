S = input("Xâu S?: ")
s = list(S)
contain = 0
for i in range(len(s)):
    if str(s[i]).isdigit()==True:
        contain = 1
print("S có chứa chữ số") if contain == 1 else print("S không chứa chữ số")