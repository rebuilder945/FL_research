ls1=list(eval(input()))
n,m=eval(input())
if n<=m and m<=len(ls1):
   ls1[n:m] = []
   print(ls1)
else:
    print('error')
