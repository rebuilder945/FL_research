ls=list(eval(input()))
n,m=eval(input())
a=ls[n]
if n>len(ls)-1:
    print("error")
else:
    for x in range(m):
        ls.append(a)
    print(ls)
