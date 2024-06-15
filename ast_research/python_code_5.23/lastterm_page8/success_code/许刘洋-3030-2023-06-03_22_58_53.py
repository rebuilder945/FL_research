def hanshu(x):
    return x[1]
a=list(input().split(','))
b=list(input().split(','))
c=[]
for i in range(len(a)):
    d=[]
    d.append(a[i])
    d.append(eval(b[i]))
    c.append(d)
c.sort(key=hanshu)
print(c)
