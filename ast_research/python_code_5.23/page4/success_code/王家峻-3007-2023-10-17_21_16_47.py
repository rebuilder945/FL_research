ls1=list(eval(input()))
n,m=eval(input())
if m<=len(ls1):
   ls1[n:m] = []
else:
    print('error')
