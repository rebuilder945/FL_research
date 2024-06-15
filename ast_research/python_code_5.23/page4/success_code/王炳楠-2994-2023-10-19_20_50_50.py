ls3=input().split(",")
ls=[int(i) for i in ls3]
ls2=ls.copy()

n,m=eval(input())
l=len(ls)
if n>l-1 or n<(-1)*l:
    print("error")
else:
    for i in range(m):
        ls2.append(ls[n])
    print(ls2)
