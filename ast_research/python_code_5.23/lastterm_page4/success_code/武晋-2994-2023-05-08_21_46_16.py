ls=list(eval(input()))
n,m=eval(input())
if n >=len(ls) or n <-len(ls):
    print("error")
else:
    K=(ls[n])*m
    ls.append(K)
    print(ls)

