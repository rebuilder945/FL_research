lst=eval(input())
n,m=eval(input())
lst2=[]
if 0<=n<=len(lst) or -len(lst)<=n<=0:
    lst2.append(lst[n])
    lst2*m
    lst.extend(lst2)
else:
    print(error)
