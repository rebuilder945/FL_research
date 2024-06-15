a=eval(input())
n,m=eval(input())
b=len(a)
if m in range(b):
    del a[n:m+1]
    print(a)
else:
    print("error")
