a=input().split(",")
b=eval(input())
c=[]
for x in range(len(a)):
    c.append([a[x],b[x]])
c=c.sort(key=lambda c: c[1])
print(c)





