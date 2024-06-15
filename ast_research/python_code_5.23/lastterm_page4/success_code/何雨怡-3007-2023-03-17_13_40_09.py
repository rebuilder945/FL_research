lst=eval(input())
n,m=eval(input())
max=len(lst)
if n>=max-1 or m>=max-1:
    print('error')
else:
    newlist1=lst[0:n+1]
    newlist2=lst[m+1:]
    newlist=newlist1+newlist2
    print(newlist)
