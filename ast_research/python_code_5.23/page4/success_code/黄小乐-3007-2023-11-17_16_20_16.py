ls=eval(input())
n,m=input().split(",")
n=int(n)
m=int(m)
ls=list(ls)
for i in range(n,m):
    ls.pop(i)
print(ls)


