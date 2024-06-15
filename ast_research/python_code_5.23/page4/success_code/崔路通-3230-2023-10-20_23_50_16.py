a=eval(input())
a.sort()
c=0
for i in range(len(a)):
    c=c+a[i]*10**i
print(c)


