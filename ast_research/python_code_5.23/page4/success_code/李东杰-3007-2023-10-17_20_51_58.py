a=eval(input())
n,m=eval(input())
b=list(range(n,m))
c=len(a)-1
if m<=c:
    for x in b:
        del a[x]
        print(a)
elif n>m:
    print("error")
else:
    print("error")

