a=input().split(",")
b=eval(input())
c=[]
for x in range(len(a)):
    d=[a[x],b[x]]
    c.append(d)
c.sort(key=lambda x:x[1], reverse=False)
print(c)

