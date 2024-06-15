a=eval(input())
n,m=eval(input())
if n>len(a) or m>len(a):
    print("error")
elif n<=len(a) and m<=len(a):
    del a[n:m]
    print(a)    
