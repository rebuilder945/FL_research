lst=eval(input())
n,m=eval(input())
if n not in lst or m not in lst:
    print("error")
else:
    a=lst.index(lst[n])
    b=lst.index(lst[m])
    lst.remove(lst[a:b])
    print(lst)
