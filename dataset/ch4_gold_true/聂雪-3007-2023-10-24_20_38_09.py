a=eval(input())
n,m=eval(input())
if n<=len(a)-1 and m<=len(a)-1:
   del a[n:m]
   print(a)
else:
    print('error')
