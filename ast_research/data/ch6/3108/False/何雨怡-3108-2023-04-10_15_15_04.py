lst=eval(input())
empty=[]
order=[]
for i in lst:
    new=list(i)
    for x in new:
        empty.append(x)
empty.sort()
newlist=list(set(empty))
newlist.sort()
for i in newlist:
    counter=empty.count(i)
    print(i,counter)

