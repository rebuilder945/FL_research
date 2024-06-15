lst=eval(input())
lst1=lst.reserve()
a=[]
for i in range(0,len(lst1)):
    b=lst.index(i)
    a.append(lst1[b])
    c=a.reverse()
    d=c.split(" ")
    print(d)

