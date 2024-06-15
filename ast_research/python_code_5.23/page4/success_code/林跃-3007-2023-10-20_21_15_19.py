lst=eval(input())
n,m=eval(input())
if n not in lst or m not in lst:
    print("error")
else:
    a=eval(lst.index(lst[n::]))
    b=eval(lst.index(lst[m::]))
    lst.remove(lst[a+1:b])
    print(lst)
