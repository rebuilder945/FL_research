n=int(input())
l=[]
x=2
y=1
i=1
while i<=n:
    l.append(x/y)
    x=x+y
    y=x-y
    i+=1
print('%.4f'%sum(l))

