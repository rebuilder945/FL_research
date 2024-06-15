ls=eval(input())
n,m=eval(input())
if n and m in ls:
   del ls[n:m]
   print(ls)
else:
    print("error")
