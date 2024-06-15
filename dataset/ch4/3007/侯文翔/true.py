ls=eval(input())
n,m=eval(input())
if n<len(ls) and m<len(ls):
    del ls[n:m]
    print(ls)
else:
    print("error")
