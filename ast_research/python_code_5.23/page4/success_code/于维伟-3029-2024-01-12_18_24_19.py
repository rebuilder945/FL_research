a=input().split(',')
a=list(a)
b=input()
c=[]
for x in range(len(a)):
    n=[]
    n.append(a[x])
    n.append(b[x])
    c.append(n)
print(c)
