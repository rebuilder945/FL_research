a=list(input().split(','))
b=list(input().split(','))
c=[]
for i in range(len(a)):
    d=[a[i],eval(b[i])]
    c.append(d)
c.sort(key=lambda x:x[1])
print(c)
