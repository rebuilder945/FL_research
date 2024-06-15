a=list(input())
for x in range(0,len(a)):
    a[x]=(a[x]+5)%10
print(','.join(str(i) for i in a))


