n=input()
a=0
b=[]
for i in n:
    if n.count(i)==1:
        b.append(i)
        a=1
if a==1:
    print(''.join (b[0]))
else:
    print('None')

