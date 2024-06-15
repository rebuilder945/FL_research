ls=list(eval(input()))
n,m=eval(input())
for i in range(m):
    if n>=len(ls) or n<-len(ls):
        print("error")
    else:
        ls.pop(n-1)
        ls.append(ls.pop(n-1))
        print(ls)
