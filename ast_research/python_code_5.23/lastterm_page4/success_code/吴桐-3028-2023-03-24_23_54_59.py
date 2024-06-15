def dengcha(n,m,l):
    li=[]
    for i in range(m):
        x=n+l*i
        li.append(x)
    return li
a=eval(input())
n=a[0]
m=a[1]
l=a[2]
shuchu=dengcha(n,m,l)
print(shuchu)
