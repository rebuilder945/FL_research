
a=input().split(",")
b=eval(input())
m=len(a)
# d=[[x+y for x in a for y in b]]
d=[]
for x in range(m):
    m=a[x]
    n=b[x]
    c=[m,n]
    d.append(c)
print(d)
# print(a)
# print(b)
# print(m)
