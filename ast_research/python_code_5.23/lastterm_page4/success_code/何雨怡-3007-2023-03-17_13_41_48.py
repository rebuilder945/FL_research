lst=eval(input())
n,m=eval(input())
a=max(n,m)
b=min(n,m)
max=len(lst)
if b>=max-1:
    print('error')
else:
    newlist1=lst[0:n+1]
    newlist2=lst[m+1:]
    newlist=newlist1+newlist2
    print(newlist)
