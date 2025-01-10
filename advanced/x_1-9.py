d=[]
for i in range(1000, 10000):
    if "0" in list(str(i)):
        continue
    else:
        #if len(set(str(i))) == 4:
            if i%6==0:
                d.append(i)
print(d)
print(len(d))