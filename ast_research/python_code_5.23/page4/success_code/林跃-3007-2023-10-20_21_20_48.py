lst=eval(input())
n,m=eval(input())
if n not in lst or m not in lst:
    print("error")
else:
    a=lst.index(n)
    b=lst.index(m)
    lst.delet(lst[a+1:b])
    print(lst)
