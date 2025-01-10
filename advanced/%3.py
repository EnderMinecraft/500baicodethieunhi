import time
start_time = time.time()
d=[]
for i in range(100,477):
    if i%2==0:
        if len(set(str(i)))==3:
            d.append(i)
print(d)
print(len(d))
print("--- %s seconds ---" % (time.time() - start_time))