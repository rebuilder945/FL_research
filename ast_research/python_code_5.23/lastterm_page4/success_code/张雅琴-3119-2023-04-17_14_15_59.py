lst=eval(input())
lst.reverse()
a=[]
for i in lst:
    b=lst.index(i)
    a.append(lst[b])
    a.reverse()
    d=a.split(" ")
    print(d)

