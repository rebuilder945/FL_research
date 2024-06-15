a=list(input().split(","))
b=eval(input())
c=[]
for n in range(0,len(a)+1):
    c.append([a[n],b[n]])
print(c)

