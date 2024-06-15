n = int(input())
ls1 = []
for x in range(1,n+1):
    ls1.append(x)
for i in range(len(ls1)-1):
    ls1[i],ls1[i+1] = ls1[i+1],ls1[i]
print(ls1)


