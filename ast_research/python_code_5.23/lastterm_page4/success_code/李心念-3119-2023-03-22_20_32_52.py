a1 = input()
a = a1[1:-1].split(",")
b = a.copy()
for i in range(len(a)-1):
    for x in range(a.count(b[i])-1):
        # if a.count(b[i])==1:
        #     break
        a.remove(b[i])
print(a)


