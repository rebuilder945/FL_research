a =list(eval(input()))
a.sort()
b=[]
for i in a:
    if i.count()==1:
        b.append(i)
if len(b)==0:
    print('False')
else:
    print(b)
