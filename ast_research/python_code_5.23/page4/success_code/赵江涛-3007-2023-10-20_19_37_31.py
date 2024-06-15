ls = eval(input())
n,m = eval(input())
if n>=0 and m+1 <=len(ls) :
    del ls[n:m]
    print(ls)
else: print('error')
