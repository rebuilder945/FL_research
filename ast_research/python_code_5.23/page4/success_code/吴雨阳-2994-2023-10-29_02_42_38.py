ls=list(eval(input()))
n,m=eval(input())
if n>len(ls) or n<-len(ls):
    print("error")
else:
    a=ls[n]
    for i in range(m):
        ls.append(a)
    print(ls)
