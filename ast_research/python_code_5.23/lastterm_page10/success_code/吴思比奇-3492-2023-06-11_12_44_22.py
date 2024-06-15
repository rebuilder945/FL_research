a=list(input())
q=[]
for i in a:
    if a.count(i)==1:
        q.append(i)
if q==[]:
    print('None')
else: 
    print(q[0])


