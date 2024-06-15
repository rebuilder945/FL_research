a=eval(input())
n,m=eval(input())
if n>len(a) or m>len(a):
    print("Error")
elif n<=len(a) and m<=len(a):
    del a[n:m]
    print(a)    
