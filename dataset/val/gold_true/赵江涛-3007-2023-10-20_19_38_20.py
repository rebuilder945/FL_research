ls = eval(input())
n,m = eval(input())
if n<=m and    n>=0 and m <=len(ls) :
    del ls[n:m]
    print(ls)
else: print('error')
