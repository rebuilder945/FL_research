a=list(input().split(","))
b=eval(input())
c=[]
for n in range(1,len(a)+1):
    d=list(a[n],b[n])
    c.append(d)
print(c)

