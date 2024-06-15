c=input()
a=list(map(int(c)))
b=[]
for x in range(len(a)):
    if a.account(a[x])==1:
        b.append(a[x])
b.sort()
print(b)

