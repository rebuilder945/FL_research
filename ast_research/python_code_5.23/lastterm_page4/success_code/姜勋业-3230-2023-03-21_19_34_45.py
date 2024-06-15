a=eval(input())
a.sort()
k=len(a)
m=0
for i in range(len(a)):
    x=a[i]
    m=m+x*10**i
print(m)
