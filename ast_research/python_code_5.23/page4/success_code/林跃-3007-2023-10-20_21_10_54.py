lst=eval(input())
n,m=eval(input())
if n not in lst or m not in lst:
    print("error")
else:
    a=index(lst[n])
    b=index(lst[m])
    lst.remove(lst[a:b])
    print(lst)
