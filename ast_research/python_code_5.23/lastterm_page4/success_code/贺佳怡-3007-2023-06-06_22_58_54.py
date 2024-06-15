a=eval(input())
n,m=eval(input())
sum=0
if len(a)>n:
    i=0
    for i in range(n,m):
        a.pop(i)
print(a)

