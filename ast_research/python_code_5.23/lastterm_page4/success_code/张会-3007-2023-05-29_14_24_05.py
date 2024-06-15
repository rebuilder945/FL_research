ls=eval(input())
n,m=eval(input())
if n>=len(ls) or m>=len(ls):
    print('error')
else:
    del ls[n:m]
    print(ls)
