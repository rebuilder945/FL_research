lst=input()
n,m=eval(input())
if n or m in lst:
  del lst[n:m]
  print(lst)
else:
    error

