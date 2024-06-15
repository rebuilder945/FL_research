lst=list(eval(input()))
n,m=eval(input())
if n<-len(lst) or n>=len(lst):
    print("error")
else:
    a=lst[n]
    for i in range(m):
        lst.append(a)
    print(lst)
