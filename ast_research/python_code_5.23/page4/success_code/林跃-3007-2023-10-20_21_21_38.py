lst=eval(input())
n,m=eval(input())
if n not in lst or m not in lst:
    print("error")
else:
    lst1=[]
    a=lst.index(n)
    b=lst.index(m)
    lst1.pop(lst[a+1:b])
    print(lst)
