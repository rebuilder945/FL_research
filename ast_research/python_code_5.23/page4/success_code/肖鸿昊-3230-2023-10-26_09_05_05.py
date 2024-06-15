a=eval(input())
a.sort()
b=len(a)
c=0
for i in range(b):
    c=c+a[i]*10**i
print(c)
