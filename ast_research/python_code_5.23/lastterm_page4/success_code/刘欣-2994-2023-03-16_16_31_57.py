ls=list(eval(input()))
n,m=eval(input())
a=ls[n]
if n>=len(ls) or n<-len(ls):
    print("error")
else:
    count=0
    while count<m:
        ls.remove(a)
        ls.append(a)
    print(ls)
