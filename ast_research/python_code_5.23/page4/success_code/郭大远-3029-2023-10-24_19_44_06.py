a=input().split(",")
b=eval(input())
c=[]
for x in list(range(len(a))):
    n=[a[x],b[x]]
    c.append(n)
print(c)


