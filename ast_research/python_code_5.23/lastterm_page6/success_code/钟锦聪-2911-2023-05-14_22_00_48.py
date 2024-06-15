a = list(map(int,input()))
for i in range(len(a)):
    a[i] = (a[i]+5)%10
for x in range(len(a)//2):
    a[x],a[-1-x]=a[-1-x],a[x]
print(*a,sep="")
