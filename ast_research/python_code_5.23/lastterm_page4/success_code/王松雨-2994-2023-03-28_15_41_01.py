lst=input().split(',')
n,m=eval(input())
l=len(lst)
if n>=l or n<-l:
    print("error")
else:
    for x in range(m):
        a=lst[n]
        lst.append(a)
    print(lst)
