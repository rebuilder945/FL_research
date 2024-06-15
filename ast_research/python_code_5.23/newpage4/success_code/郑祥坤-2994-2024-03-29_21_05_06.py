a=eval(input())
n,m=eval(input())
l=len(a)
if n >=l or n <-1*l:
    print("error")
else:
    b=[a[n]]*m
c=[x for x in a]
print(c+b)
