S = input("Xâu S?")
if len(list(S)) < 3:
    print("Nhập sai định dạng")
else:
    print(list(S)[0]+list(S)[1]+list(S)[2])