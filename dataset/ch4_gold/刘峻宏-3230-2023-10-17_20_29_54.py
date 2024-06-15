a=eval(input())
a.sort()
b=1
s=0
for i in range(len(a)):
    s+=a[i]*b
    b=b*10
