lst=list(map(int,input().split(',')))
n,m=eval(input())
l=len(lst)
if n>=l or n<-l:
    print("error")
else:
    for x in range(m):
        a=int(lst[n])
        lst.append(a)
    print(lst)
