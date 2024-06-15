lst=eval(input())
n,m=eval(input())
lst1=lst[n:m]
ls=[]
if 0<=n<m<=len(lst):
    for i in lst:
        if i not in lst1:
            ls.append(i)
    print(ls)
else:
    print('error')
