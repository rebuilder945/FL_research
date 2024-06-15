a=eval(input())
c=[]
for i in a:
    b=a.count(i)
    if b==1:
        c.append(i)
c.sort()
c=','.join(str(i) for i in c)
print(c)


