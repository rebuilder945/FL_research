ls=list(eval(input()))
n,m=eval(input())
if -len(ls)<=n<=len(ls)-1:
    k=ls[n]
    for i in range(m):
        ls.append(k)
    print(ls)
if n<-len(ls) or n>=len(ls):
    print('error')
