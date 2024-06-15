ls = list(eval(input()))
n,m=eval(input())
if -len(ls)<=n<=len(ls)-1:
    a=ls[n]
    for x in range(m):
        ls.append(a)
    print(ls)
else:
    print("error")
