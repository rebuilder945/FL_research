lst=eval(input())
n,m=eval(input())
if n<len(lst):
    ls=lst[n:m]
    for x in lst:
        if x in ls:
            lst.remove(x)
    print(lst)
else:
    print('error')
