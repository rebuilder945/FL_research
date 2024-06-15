lst=list(map(int,input().split(',')))
n,m=eval(input())
l=len(lst)
if n>=l or n<-l:
    print("error")
else:
    a=lst[n]
    for x in range(m):
        lst.append(a)
    print(lst)
