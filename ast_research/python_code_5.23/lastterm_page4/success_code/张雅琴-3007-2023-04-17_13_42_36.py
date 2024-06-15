lst=eval(input())
n,m=eval(input())
l=len(lst)-1
if n<=l and m<=l:
    if n<=m:
       lst2=[] 
       lst2.append(i for i in range (n,m))
       lst2.reverse()
    for x in lst2:
       lst.pop(x)
    print(lst)
else:
    print('error')

