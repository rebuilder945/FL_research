n=int(input())
i=1
j=1
k=1
while n>0:
    a=(i+k)/j
    j+=k
    i+=(k-1)
    k+=1
    n-=1
print('%.4f'%a)


