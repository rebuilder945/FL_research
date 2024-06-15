a=list(input())
b=list(input())
c=[]
for x in range(len(a)):
    d=[a[x],eval(b[x])]
c.sort(key=lambda x:x[1])
print(c)
