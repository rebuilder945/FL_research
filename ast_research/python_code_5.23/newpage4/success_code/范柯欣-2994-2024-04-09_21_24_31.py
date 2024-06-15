lst=list(eval(input()))
n,m=eval(input())
if n>=len(lst)+1:
    print("error")
else:
    for i in range(m):
        if n>=-1:
            lst.append(lst[n])
        elif n<-1:
            lst.append(lst[n])
            n=n-1
    print(lst)

