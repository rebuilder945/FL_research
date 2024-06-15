a=eval(input())
n,m=eval(input())
if n<=len(a)-1 and m<=len(a)-1:
    if n<=m:
        del a[n:m]
    else:
        del a[n:m:-1]  
    print(a)  
else: print("error")
