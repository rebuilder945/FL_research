a=eval(input())
n,m=eval(input())
if n<=m and n>=0 and m<=len(a):
    del a[n:m:1]
    print(a)
else:
    print("error")
    
