a=eval(input())
n,m=eval(input())
if n<len(a) or m<n:
    print("error")
else:
    del a[n,m]
print(a)

