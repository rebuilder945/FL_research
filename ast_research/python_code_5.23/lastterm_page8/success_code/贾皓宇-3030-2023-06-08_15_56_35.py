a=eval(input())
b=eval(input())
c=[]
for i in range(len(a)):
    d=[a[i],b[i]]
    c.append(d)
c.sort()
print(c)
