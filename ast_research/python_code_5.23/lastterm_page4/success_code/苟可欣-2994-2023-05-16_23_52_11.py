ls=list(eval(input()))
n,m=eval(input())
if n>len(ls)-1:
    print("error")
else:
    for x in range(m):
        x=ls[n]
        ls.append(x)
    print(ls)
