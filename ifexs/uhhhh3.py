rangepg = range(1,99999)
numpg = 0
for i in rangepg:
    if (i<=9 and numpg<3249):
        numpg = numpg + 1
        out = i
    if(10<=i<=99 and numpg<3249):
        numpg = numpg + 2
        out = i
    if(100<=i<=999 and numpg<3249):
        numpg = numpg + 3
        out = i
    if(1000<=i<=9999 and numpg<3249):
        numpg = numpg + 4
        out = i
    if(10000<=i<=99999 and numpg<3249):
        numpg = numpg + 5
        out = i
    else:
        pass
print(out)
input()