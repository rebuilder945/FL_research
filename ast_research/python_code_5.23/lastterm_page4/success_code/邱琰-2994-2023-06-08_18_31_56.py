ls=list(eval(input()))
n,m=eval(input())
if -len(ls)<=n<=len(ls)-1:
    for i in range(m):
        ls.append(ls[n])
    print(ls)
if n<-len(ls) or n>len(ls)-1:
    print('error')
