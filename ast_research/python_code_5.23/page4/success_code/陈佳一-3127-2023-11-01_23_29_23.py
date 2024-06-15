b=eval(input())
a=[]
for x in range(1,b+1):
    a.append(x)
for n in range(b):
    a[0]=a[-1]
print(a)


