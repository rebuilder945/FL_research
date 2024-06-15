ls=list(eval(input()))
n,m=eval(input())

if n>len(ls)-1:
    print("error")
else:
    a=ls[n]
    for x in range(m):
        ls.append(a)
    print(ls)
