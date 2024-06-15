ls = eval(input())
n,m = eval(input())
if  m<=len(ls) :
    del ls[n:m]
    print(ls)
else: print('error')
