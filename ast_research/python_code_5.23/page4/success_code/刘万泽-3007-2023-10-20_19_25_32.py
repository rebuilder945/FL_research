a=eval(input())
n=int(input())
m=int(input())
if n>len(a) or m>len(a):
    print("Error")
elif n<=len(a) and m<=len(a):
    del a[n:m]
    print(a)    
