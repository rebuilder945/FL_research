a=eval(input(""))
n,m=eval(input(""))
if n<=len(a) and m<=len(a):
    del a[n:m]
    print(a)
else:
    print("error")   
  

