b=input()
c=b.split(' ')
d=[c[1],c[2],c[3]]
d.sort(reverse=True)
e=(int(c[1])+int(c[2])+int(c[3]))/3
d.insert(0,c[0])
d.append(e)
for i in d:
    if type(i) is int:
        print('%.2f'%i,end=" ")
    elif type(i) is str:
        print(i,end=' ')
