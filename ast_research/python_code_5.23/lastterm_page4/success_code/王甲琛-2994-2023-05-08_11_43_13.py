a=input().split(',')
n,m=eval(input())
lst=[]
for i in a:
    lst.append(i)
lst2=[]
if 0<=n<=len(lst) or -len(lst)<=n<=0:
    lst2.append(lst[n])
    lst.extend(lst2*m)
    for i in range(len(lst)):
        lst[i]=int(lst[i])
    print(lst)
else:
    print("error")
