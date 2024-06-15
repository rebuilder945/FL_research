ls=list(eval(input()))
n,m=eval(input())
if n>=len(ls) or n<-len(ls):
    print("error")
else:
    count=0
    while count<m:
        ls.pop(n)
        ls.append(ls.pop(n))
    print(ls)
