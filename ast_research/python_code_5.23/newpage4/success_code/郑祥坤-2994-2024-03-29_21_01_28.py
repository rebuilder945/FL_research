a=eval(input())
n,m=eval(input())
if n not in range(len(a)):
    print("error")
else:
    b=[a[n+1]]*m
c=[x for x in a]
print(c+b)
