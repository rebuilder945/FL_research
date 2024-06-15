lst=eval(input())
lst.reserve()
a=[]
for i in range(0,len(lst)):
    b=lst.index(i)
    a.append(lst[b])
    a.reverse()
    d=a.split(" ")
    print(d)

