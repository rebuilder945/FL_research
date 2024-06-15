a=list(input().split(","))
b=list(input().split(","))
c=[]
for i in range(0,len(a)):
    x=[a[i],eval(b[i])]
    c.append(x)
print(c)
