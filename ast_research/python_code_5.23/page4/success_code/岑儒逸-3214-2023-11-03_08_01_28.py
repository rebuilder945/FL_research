ls=eval(input())
n=0
for i in ls:
    if i==0:
        n=n+1
        ls.remove(i)
m=0
while n>0:
    ls.append(0)
    n=n-1
print(ls)

