b=int(input())
a=[b]
for x in range(0,len(a)):
    a[x]=(a[x]+5)%10
a[0],a[1]=a[-1],a[-2]
print(str(a))


