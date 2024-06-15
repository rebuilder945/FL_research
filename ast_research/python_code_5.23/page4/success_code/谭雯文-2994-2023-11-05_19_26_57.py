ls=list(eval(input()))
n,m=eval(input())
a=ls[n]
if -len(ls)<n <len(ls):

    for i in range(m):
        ls.append(a)
    print(ls)
else:
    print("error")



