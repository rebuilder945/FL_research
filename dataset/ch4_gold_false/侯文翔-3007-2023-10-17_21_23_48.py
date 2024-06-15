ls=eval(input())
n,m=eval(input())
if n<len(ls) and m<len(ls) and n<m:
    del ls[n:m]
    print(ls)
else:
    print("error")
