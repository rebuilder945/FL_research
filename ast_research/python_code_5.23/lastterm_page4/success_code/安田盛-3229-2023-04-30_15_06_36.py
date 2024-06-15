n=eval(input())
m=[]
for i in n:
    if n.count(i)==1:
        m.append(i)
if m==[]:
    print('False')
else:
    m.sort()
    print(*m,sep=",")
    








