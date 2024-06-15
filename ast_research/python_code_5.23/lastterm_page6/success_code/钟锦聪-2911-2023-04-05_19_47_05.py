a = list(map(int,input()))
for i in range(len(a)):
    a[i] = (a[i]+5)%10
if len(a)%2==0:
    for x in range(len(a)/2):
        a[x],a[-1-x]=a[-1-x],a[x]
else:
    for x in range(len(a)//2+1):
        a[x],a[-1-x]=a[-1-x],a[x]
print(*a,sep="")
