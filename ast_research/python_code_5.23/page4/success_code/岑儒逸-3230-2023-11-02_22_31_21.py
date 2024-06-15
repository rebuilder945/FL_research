ls=eval(input())
n=len(ls)
m=0
a=0
while m<n:
    a=a+max(ls)*10**(n-1)
    ls.remove(max(ls))
    n=n-1
print(a)
