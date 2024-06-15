a=eval(input())
n,m=eval(input())
lst=[]
for i in a:
    lst.append(i)
lst2=[]
if 0<=n<=len(lst) or -len(lst)<=n<=0:
    lst2.append(lst[n])
    lst2*m
    lst.extend(lst2)
else:
    print(error)
