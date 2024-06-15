lst=eval(input())
n,m=eval(input())
lst1=lst[n:m]
n=n-1
m=m-1
ls=[]
if n in range(len(lst)) and m in range(len(lst)):
    for i in lst:
        if i not in lst1:
            ls.append(i)
    print(ls)
else:
    print('error')
