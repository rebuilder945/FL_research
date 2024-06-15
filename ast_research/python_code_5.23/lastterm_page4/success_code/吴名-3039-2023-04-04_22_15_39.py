lst=eval(input())
if len(lst)==0:
    print("[]")
else:
    a=max(lst)
    b=min(lst)
    c=lst.count(a)
    d=lst.count(b)
    lst1=[]
    for i in range(0,c):
        lst1.append(a)
    for i in range(0,d):
        lst1.append(b)
    if len(lst)>len(lst1):
        for i in range(0,c):
            lst.remove(a)
        for i in range(0,d):
            lst.remove(b)
    else:
        lst=[]
    print(lst)
