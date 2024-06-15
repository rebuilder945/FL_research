a=list(input().split(' '))
b,c=input().split(' ')
e=int(b)
f=int(c)
for x in a[e:e+1]:
    m=x
for y in a[f:f+1]:
    n=y
a[e]=n
a[f]=m
print(a)
