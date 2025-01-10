S = list(input("S: "))
rm = input("rm: ")
rm = rm.split()
for i in range(len(rm)):
    S_copy = S[:]
    for j in range(len(S_copy)):
        if S_copy[j] == rm[i]:
            S.remove(S_copy[j])
print("".join(S))