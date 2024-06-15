b=input()
c=b.split(' ')
d=[c[1],c[2],c[3]]
d.sort(reverse=True)
e=(c[1]+c[2]+c[3])/3
d.insert(0,c[0])
d.append(e)
for i in d:
    print('%.2f',i,end=" ")
