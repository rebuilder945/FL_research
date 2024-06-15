lst=eval(input())
n,m=eval(input())
a=max(n,m)
b=min(n,m)
max=len(lst)
if a>=max-1:
    print('error')
else:
    newlist1=lst[:b+1]
    newlist2=lst[a+1:]
    newlist=newlist1+newlist2
    print(newlist)
