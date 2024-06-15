a=list(input())
for x in range(len(a)):
    a[x]=(a[x]+5)%10
print(a,end='')


