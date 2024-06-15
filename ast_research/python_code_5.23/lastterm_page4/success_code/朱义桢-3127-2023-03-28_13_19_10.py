a=eval(input())
b=[e for e in range(1,a+1)]
d=[]
for x in b:
    m=x%a
    d.append(b[m])
print(d)
