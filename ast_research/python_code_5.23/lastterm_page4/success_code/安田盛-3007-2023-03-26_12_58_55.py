lst=eval(input())
n,m=eval(input())
lst1=lst.copy()
if n<=m<=len(lst):
    for i in lst[n:m]:
        lst1.remove(i)
    print(lst1)
else:
    print('error')
