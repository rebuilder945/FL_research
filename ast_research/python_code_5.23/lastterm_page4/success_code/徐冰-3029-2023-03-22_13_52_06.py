a=input().split(',')
b=eval(input())
c=[]
for x in range(len(b)):
    ls=[]
    ls.append(a[x])
    ls.append(b[x])
    c.append(ls)
print(c)
