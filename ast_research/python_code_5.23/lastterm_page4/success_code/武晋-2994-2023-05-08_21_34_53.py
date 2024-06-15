ls=list(eval(input()))
n,m=eval(input())
if n >=len(ls) or n <-len(ls):
    print("error")
else:
    append_l=(ls[n])*m
    ls=ls+append_l
    print(ls)

