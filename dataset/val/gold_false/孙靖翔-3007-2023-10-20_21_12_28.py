ls=eval(input())
n,m=eval(input())
n<=m
if n and m in ls:
  del ls[n:m]
  print(ls)
elif n or m not in ls:
    print("error")

