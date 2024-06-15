ls=list(eval(input()))
n,m=eval(input())
for i in range(len(ls)):
    if n>=len(ls) or n<-len(ls):
        print("error")
    else:
        ls.pop(n)
        count=0
        while (count<m):
            ls.append(ls.pop(n))
print(ls)
