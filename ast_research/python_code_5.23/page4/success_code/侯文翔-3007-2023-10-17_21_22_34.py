ls=eval(input())
n,m=eval(input())
if n-1<=len(ls) and m-1<=len(ls) and n<m:
    del ls[n:m]
    print(ls)
else:
    print("error")
