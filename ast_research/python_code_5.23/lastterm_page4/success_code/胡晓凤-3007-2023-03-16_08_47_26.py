a=eval(input())
lst=[a]
n,m=eval(input())
if n<=m in lst:
    del lst[n,m-1]
    print(lst)
else:
    print("error")
