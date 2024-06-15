ls=eval(input())
ls=list(ls)
n,m=eval(input())
x=int(len(ls))
if -(x+1)<n<x:
    for i in range(m):
        ls.append(ls[n])
    print(ls)
else:
    print('error')
