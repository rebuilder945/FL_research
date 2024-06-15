n=eval(input())
a=[]
for x in range(1,n+1):
    a.append(x)
b=a[0]
a.pop(0)
a.insert(-1,b)
a[-1],a[-2]=a[-2],a[-1]
print(a)
