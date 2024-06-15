a=list(eval(input()))
a.sort()
c=0
for i in range(len(a)):
    c+=a[i]*10**i
print(c)
