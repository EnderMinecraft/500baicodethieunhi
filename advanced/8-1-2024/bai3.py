s1 = input("S1 str: ")
s2 = input("S2 str: ")
fs = ""
for i in range(len(s2)//2):
    fs = fs + s2[i]
fs = fs +s1
for i in range(len(s2)//2, len(s2)):
    fs = fs + s2[i]
print(fs)