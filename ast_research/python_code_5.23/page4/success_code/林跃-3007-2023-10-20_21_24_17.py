lst=eval(input())
n,m=eval(input())
if n not in lst or m not in lst:
    print("error")
else:
    lst1=[]
    a=lst.index(n)
    b=lst.index(m)
    lst1.append(lst[0:a+1] and lst[b::])
    print(lst1)
