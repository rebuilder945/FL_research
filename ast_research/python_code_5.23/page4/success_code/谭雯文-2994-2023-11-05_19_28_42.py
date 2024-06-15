ls=list(eval(input()))
n,m=eval(input())
if -len(ls)<n <len(ls):
    a=ls[n]
    for i in range(m):
        ls.append(a)
    print(ls)
else:
    print("error")



