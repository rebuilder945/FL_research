ls=list(eval(input()))
n,m=eval(input())
for i in range(m):
    if n>=len(ls) or n<-len(ls):
        print("error")
        break
    else:
        ls.pop(n)
        ls.append(ls.pop(n))
    print(ls)
