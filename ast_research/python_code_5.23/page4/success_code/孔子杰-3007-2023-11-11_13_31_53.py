lst=eval(input())
n,m=eval(input())
if n<=m and m<=len(lst)-1 and n>=0:
   lst[n:m]=[]
   print(lst)
else:
   print("error")
