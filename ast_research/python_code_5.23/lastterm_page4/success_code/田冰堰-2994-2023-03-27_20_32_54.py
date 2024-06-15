ls=eval(input())
n,m=eval(input())
a=len(ls)
if n>=a:
    print("error")
else:
    ls.append(ls[n]*m)
    print(ls)
