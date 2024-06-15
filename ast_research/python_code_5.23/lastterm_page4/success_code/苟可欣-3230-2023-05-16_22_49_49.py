ls=eval(input())
ls.sort()
k=0
for x in range(len(ls)):
    k=k+ls[x]*(10**x)
print(k)

