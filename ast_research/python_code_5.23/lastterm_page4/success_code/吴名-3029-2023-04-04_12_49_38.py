a=list(input().split(","))
b=eval(input())
print(b)
c=[]
for i in range(0,len(a)):
    x=[a[i],b[i]]
    c.append(x)
print(c)
