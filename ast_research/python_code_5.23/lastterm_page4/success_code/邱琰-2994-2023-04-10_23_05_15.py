lst=list(eval(input()))
n,m=eval(input())
if n>=len(lst) or n<-len(lst):
    print("error")
else:
    k=lst[n]
    for x in range(m):
        lst.append(k)
    print(lst)
