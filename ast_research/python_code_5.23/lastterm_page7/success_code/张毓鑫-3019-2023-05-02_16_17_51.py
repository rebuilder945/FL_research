b=eval(input())
c=b.split(' ')
d=[c[1],c[2],c[3]]
d.sort(reverse=True)
d.insert(0,c[0])
for i in d:
    print(i,end=" ")
